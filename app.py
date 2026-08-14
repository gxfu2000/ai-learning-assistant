import os
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader


# =========================
# 读取API
# =========================

load_dotenv()

api_key = os.getenv("DASHSCOPE_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


# 保存PDF内容
pdf_text = ""


# =========================
# PDF读取
# =========================

def upload_pdf(file):

    global pdf_text

    reader = PdfReader(file.name)

    text = ""

    for page in reader.pages:
        content = page.extract_text()

        if content:
            text += content + "\n"


    pdf_text = text


    return f"""
PDF读取完成！

总字数：
{len(pdf_text)}

现在可以提问。
"""


# =========================
# AI回答
# =========================

def ask_ai(question):

    if not pdf_text:
        return "请先上传PDF文件"


    prompt = f"""

你是一名学习助手。

下面是教材内容：

----------------

{pdf_text[:12000]}

----------------


请根据教材回答问题：

{question}


要求：
1. 优先依据教材
2. 不确定就说明
3. 用学生容易理解的方式解释

"""


    response = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )


    return response.choices[0].message.content



# =========================
# 网页界面
# =========================


with gr.Blocks(title="AI学习助手") as demo:


    gr.Markdown(
        """
# 📚 AI学习助手

上传教材PDF，
让AI帮你学习。
"""
    )


    file = gr.File(
        label="上传PDF教材"
    )


    upload_result = gr.Textbox(
        label="状态"
    )


    file.upload(
        upload_pdf,
        inputs=file,
        outputs=upload_result
    )


    question = gr.Textbox(
        label="请输入问题",
        placeholder="例如：第三章主要讲什么？"
    )


    answer = gr.Textbox(
        label="AI回答",
        lines=10
    )


    btn = gr.Button(
        "开始提问"
    )


    btn.click(
        ask_ai,
        inputs=question,
        outputs=answer
    )



demo.launch()