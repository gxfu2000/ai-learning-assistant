from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


# 中文向量模型
embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5"
)


vector_db = None



def create_database(text):

    global vector_db


    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )


    chunks = splitter.split_text(text)


    vector_db = Chroma.from_texts(
        texts=chunks,
        embedding=embedding_model,
        persist_directory="./chroma_db"
    )


    return len(chunks)





def search_context(question):

    if vector_db is None:
        return ""


    docs = vector_db.similarity_search(
        question,
        k=5
    )


    result = "\n\n".join(
        [
            d.page_content
            for d in docs
        ]
    )


    return result