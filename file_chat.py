import os
from dotenv import load_dotenv
from openai import OpenAI


# 加载.env
load_dotenv()


api_key = os.getenv("DASHSCOPE_API_KEY")


if not api_key:
    print("没有找到 DASHSCOPE_API_KEY")
    exit()


client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


response = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {
            "role": "user",
            "content": "你好，请介绍一下你自己"
        }
    ]
)


print(response.choices[0].message.content)