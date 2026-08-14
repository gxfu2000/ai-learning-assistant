import os
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter


DB_PATH = "./database"


def create_database(text):

    os.makedirs(DB_PATH, exist_ok=True)

    client = chromadb.PersistentClient(
        path=DB_PATH
    )


    collection = client.get_or_create_collection(
        name="knowledge"
    )


    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )


    chunks = splitter.split_text(text)


    # 清空旧数据
    try:
        old = collection.get()

        if old["ids"]:
            collection.delete(
                ids=old["ids"]
            )

    except:
        pass


    for i, chunk in enumerate(chunks):

        collection.add(
            ids=[str(i)],
            documents=[chunk]
        )


    return len(chunks)



def search_database(question):

    client = chromadb.PersistentClient(
        path=DB_PATH
    )


    collection = client.get_collection(
        name="knowledge"
    )


    result = collection.query(
        query_texts=[question],
        n_results=5
    )


    if result["documents"]:

        return "\n\n".join(
            result["documents"][0]
        )


    return ""