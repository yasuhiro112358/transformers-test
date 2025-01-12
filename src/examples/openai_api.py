import os
import asyncio
from dotenv import load_dotenv
from openai import OpenAI

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

def test_9_7(client: OpenAI) -> None:
    pass



def main() -> None:
    # Load environment variables
    load_dotenv()

    # Create an OpenAI client
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    # Test the API
    # test_9_3(client)
    # test_9_5(client)
    # test_9_6(client)
    test_9_7(client)



if __name__ == "__main__":
    main()