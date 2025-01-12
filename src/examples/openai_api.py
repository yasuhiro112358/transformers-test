from dotenv import load_dotenv
import os
from openai import OpenAI

def main():
    # Load environment variables
    load_dotenv()

    # Create an OpenAI client
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    messages = [
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


if __name__ == "__main__":
    main()