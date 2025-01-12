import os
import asyncio
from dotenv import load_dotenv
import openai
from openai import OpenAI
from openai import AsyncOpenAI
import tiktoken
from typing import Awaitable, Callable, TypeVar

T = TypeVar("T")

def test_9_3(client: OpenAI) -> None:
    messages: list[dict[str, str]] = [
        {
            "role": "user",
            "content": "日本で一番高い山は何？"
        },
    ]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4o",
        # temperatureは0.0から1.0の間で設定できる
        # temperatureは0.0にすると、最も確信度の高い回答を返す
        # temperature=0.0,
        temperature=1.0,
    )

    print(chat_completion.choices[0].message.content)

def test_9_5(client: OpenAI) -> None:
    messages: list[dict[str, str]] = [
        {
            "role": "user",
            "content": "数字を１から１０まで読み上げてください"
        },
    ]

    completion = client.chat.completions.create(
        # model="gpt-4o",
        model="gpt-4o-mini",
        # model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.0,
        # 生成するトークンの最大数を指定する
        # max_tokens=1,
        # max_tokens=3,
        max_tokens=10,
    )

    print(completion.choices[0].message.content)

def test_9_6(client: OpenAI) -> None:
    messages: list[dict[str, str]] = [
        {
            "role": "user",
            "content": "数字を1から10まで読み上げてください"
        },
    ]

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=1.0,
        # 終端文字を指定する
        stop="5",
    )

    print(completion.choices[0].message.content)

async def retry_on_error(
    openai_call: Callable[[], Awaitable[T]],
    max_num_trials: int = 5,
    first_wait_time: int = 10,
) -> Awaitable[T]:
    """
    Retry the OpenAI API call if an error occurs.
    """
    for i in range(max_num_trials):
        try:
            # Call the OpenAI API
            return await openai_call()
        except openai.APIError as e:
            if i == max_num_trials - 1:
                # If the maximum number of trials is reached, raise the error to break the loop
                raise # 現在の例外を再度発生させる

            # Print the error message
            print(f"Error: {e}")

            # Wait for an exponential backoff time
            wait_time_seconds = first_wait_time * (2 ** i)
            print(f"Waiting for {wait_time_seconds} seconds...")
            await asyncio.sleep(wait_time_seconds)

async def _async_batch_run_chatgpt(
    client: AsyncOpenAI,
    messages_list: list[list[dict[str, str]]],
    temperature: float,
    max_tokens: int,
    stop: str | list[str],
) -> list[str]:
    """
    並列してリクエストを送信する
    """
    # co-routineオブジェクトをlistに格納する
    tasks = [
        retry_on_error(
            openai_call=lambda x=ms: client.chat.completions.create(
                model="gpt-4o-mini",
                messages=x,
                temperature=temperature,
                max_tokens=max_tokens,
                stop=stop,
            )
        )
        for ms in messages_list
    ]

    # 並列してリクエストを送信する
    completions = await asyncio.gather(*tasks)

    return [
        c.choices[0].message.content 
        for c in completions
    ]

def batch_run_chatgpt(
    client: AsyncOpenAI,
    messages_list: list[list[dict[str, str]]],
    temperature: float = 0.0,
    max_tokens: int = None,
    stop: str | list[str] = None
) -> list[str]:
    """
    非同期処理を実行するためのwrapper関数
    """
    return asyncio.run(
        _async_batch_run_chatgpt(
            client,
            messages_list,
            temperature,
            max_tokens,
            stop
        )
    )

def test_9_9(client: AsyncOpenAI) -> None:
    messages_list = [
        [
            {
                "role": "user",
                "content": "日本の首都はどこですか？"
            },
        ],
        [
            {
                "role": "user",
                "content": "Pythonの特徴を教えてください"
            },
        ],
        [
            {
                "role": "user",
                "content": "地球の直径はどれくらいですか？"
            },
        ],
    ]

    results: list[str] = batch_run_chatgpt(client, messages_list)
    for result in results:
        print(result)

def test_9_15() -> None:
    encoding = tiktoken.encoding_for_model("gpt-4o")
    tokens: list[int] = encoding.encode("日本の首都はどこですか？")
    print(tokens)

def main() -> None:
    # Load environment variables and get it
    load_dotenv()
    api_key: str = os.environ.get("OPENAI_API_KEY")

    # Create an OpenAI client
    client = OpenAI(api_key=api_key)

    # Create an AsyncOpenAI client
    async_client = AsyncOpenAI(api_key=api_key)

    # Test the API
    # test_9_3(client)
    # test_9_5(client)
    # test_9_6(client)
    # test_9_9(async_client)
    test_9_15()



if __name__ == "__main__":
    main()