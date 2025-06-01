from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedder():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")