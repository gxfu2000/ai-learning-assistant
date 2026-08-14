from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()


client = OpenAI(

    api_key=os.getenv(
        "DASHSCOPE_API_KEY"
    ),

    base_url=
    "https://dashscope.aliyuncs.com/compatible-mode/v1"

)



def call_ai(prompt):


    result = client.chat.completions.create(

        model="qwen-plus",

        messages=[

            {
                "role":"system",
                "content":"你是一名经验丰富的老师，负责辅导学生学习。"
            },

            {
                "role":"user",
                "content":prompt
            }

        ]

    )


    return result.choices[0].message.content




# =========================
# 总结教材
# =========================

def make_summary(context):


    prompt=f"""

请根据下面教材内容，
生成一份学生学习笔记。


要求：

1. 提炼核心知识点

2. 使用分级标题

3. 标出考试重点

4. 不要加入教材之外内容


教材：

{context}

"""


    return call_ai(prompt)





# =========================
# 生成考试题
# =========================

def make_questions(context):


    prompt=f"""

根据下面教材内容，
生成考试练习题。


要求：

生成：

一、选择题 5道

二、简答题 3道

三、重点解析


答案必须依据教材。


教材内容：

{context}

"""


    return call_ai(prompt)





# =========================
# 提取重点
# =========================

def make_keypoints(context):


    prompt=f"""


请分析下面教材。


输出：

1. 必须掌握知识点

2. 容易出错地方

3. 考试可能考察方向


教材：

{context}

"""


    return call_ai(prompt)