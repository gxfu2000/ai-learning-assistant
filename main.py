import gradio as gr
import os

from pdf_reader import read_pdf
from rag import create_database, search_context


# 当前知识库文件
current_file = ""


# =========================
# 上传PDF
# =========================

def upload_pdf(file):

    global current_file

    if file is None:
        return "❌ 请先上传PDF"


    path = file.name

    current_file = os.path.basename(path)


    try:

        text = read_pdf(path)


        chunks = create_database(text)


        return f"""
✅ 知识库建立成功

文件：
{current_file}

文本长度：
{len(text)}

知识块数量：
{chunks}

可以开始提问
"""


    except Exception as e:

        return f"❌ 建库失败：{e}"



# =========================
# 聊天
# =========================

def chat(message, history):


    if not message:

        return history


    try:


        context = search_context(message)



        if context:


            answer = f"""
📚 根据知识库内容：

{context}


-----------------

🤖 AI分析：

你的问题：
{message}


以上内容来自上传教材，我会继续结合资料进行分析。
"""


        else:


            answer = """
❌ 没有找到相关知识。

请确认：
1. 是否已经建立知识库
2. 问题是否和教材内容相关
"""


    except Exception as e:

        answer = f"系统错误：{e}"



    history.append(
        {
            "role":"user",
            "content":message
        }
    )


    history.append(
        {
            "role":"assistant",
            "content":answer
        }
    )


    return history



# =========================
# 快捷功能
# =========================


def quick_question(text):

    return text



# =========================
# UI
# =========================


with gr.Blocks(
    title="AI学习助手"
) as demo:


    gr.Markdown(
        """
# 📚 AI学习助手

基于 RAG + 大语言模型的私人知识库助手

上传教材PDF，建立你的专属AI老师。
"""
    )



    with gr.Row():


        with gr.Column(scale=1):


            pdf = gr.File(
                label="上传PDF教材",
                file_types=[".pdf"]
            )


            upload_btn = gr.Button(
                "🚀 建立知识库"
            )


            status = gr.Textbox(
                label="知识库状态",
                lines=8
            )



        with gr.Column(scale=3):


            chatbot = gr.Chatbot(
                label="🤖 AI学习助手",
                height=450
            )


            msg = gr.Textbox(
                placeholder="请输入问题，例如：总结这篇文章"
            )


            with gr.Row():

                send = gr.Button(
                    "发送 ▶"
                )


                clear = gr.Button(
                    "清空聊天"
                )



    gr.Markdown(
        "## ⚡ 快捷功能"
    )


    with gr.Row():


        btn1 = gr.Button(
            "📌 提炼重点"
        )


        btn2 = gr.Button(
            "📝 生成考试题"
        )


        btn3 = gr.Button(
            "💡 解释难点"
        )



    # 事件

    upload_btn.click(
        upload_pdf,
        inputs=pdf,
        outputs=status
    )



    send.click(
        chat,
        inputs=[
            msg,
            chatbot
        ],
        outputs=chatbot
    ).then(
        lambda:""
        ,
        outputs=msg
    )



    msg.submit(
        chat,
        inputs=[
            msg,
            chatbot
        ],
        outputs=chatbot
    )



    clear.click(
        lambda:[],
        outputs=chatbot
    )



    btn1.click(
        lambda:"请提炼教材重点",
        outputs=msg
    )


    btn2.click(
        lambda:"请根据教材生成考试题",
        outputs=msg
    )


    btn3.click(
        lambda:"请解释教材中的难点",
        outputs=msg
    )



demo.launch()