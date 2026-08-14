from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()


client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)



def ask_ai(question, context):

    prompt = f"""
你是一名专业的AI学习助手。

请根据下面提供的教材内容回答用户问题。

要求：

1. 优先使用教材内容。
2. 不要编造教材没有的信息。
3. 如果教材没有相关内容，请明确说明。
4. 回答要结构清晰。


==================
教材内容：
{context}
==================


用户问题：

{question}

"""


    response = client.chat.completions.create(

        model="qwen-plus",

        messages=[

            {
                "role":"system",
                "content":"你是一个专业学习助手"
            },

            {
                "role":"user",
                "content":prompt
            }

        ],

        temperature=0.2
    )


    return response.choices[0].message.content