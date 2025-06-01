import os
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split_docs(folder_path):
    documents = []
    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)
        if file.endswith(".pdf"):
            loader = PyMuPDFLoader(path)
        elif file.endswith(".txt"):
            loader = TextLoader(path)
        else:
            continue
        documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(documents)