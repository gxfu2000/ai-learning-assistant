import gradio as gr

from pdf_reader import read_pdf
from rag import create_database, search_context
from ai_chat import ask_ai



def upload_pdf(file):

    if file is None:
        return "请选择PDF文件"


    try:

        text = read_pdf(file.name)


        chunks = create_database(text)


        return f"""
PDF上传成功！

文字长度：
{text.__len__()}

知识库建立完成！

文本块数量：
{chunks}

现在可以提问。
"""


    except Exception as e:

        return f"读取失败：{e}"





def chat(question):

    if not question:

        return "请输入问题"



    try:

        context = search_context(question)


        if not context:

            return "没有找到相关教材内容"



        answer = ask_ai(

            question,

            context

        )


        return answer



    except Exception as e:

        return f"回答失败：{e}"






with gr.Blocks(
    title="AI学习助手"
) as demo:


    gr.Markdown(
        """
# 📚 AI学习助手 RAG版

上传PDF教材，让AI基于教材回答问题。
"""
    )



    pdf = gr.File(
        label="上传PDF教材",
        file_types=[".pdf"]
    )


    status = gr.Textbox(
        label="状态"
    )


    pdf.upload(

        upload_pdf,

        inputs=pdf,

        outputs=status

    )



    question = gr.Textbox(

        label="请输入问题",

        placeholder="例如：这篇文章主要讲什么？"

    )



    button = gr.Button(
        "开始回答"
    )



    answer = gr.Textbox(

        label="AI回答",

        lines=20

    )



    button.click(

        chat,

        inputs=question,

        outputs=answer

    )





demo.launch()