from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import Pinecone as LangchainPinecone  # new import

PINECONE_API_KEY = "pcsk_qDcxm_5MWGtm1wYNMNdbtGnx2fEBENN6D2PJtLYj24ojRQa7VmqT56BR27KRg6F5aetV4"
PINECONE_INDEX_NAME = "knowledge-base"
PINECONE_REGION = "us-east-1"

def get_vector_store(embedder):
    # Initialize Pinecone client
    pc = Pinecone(api_key=PINECONE_API_KEY)

    # Create index if doesn't exist
    if PINECONE_INDEX_NAME not in pc.list_indexes().names():
        pc.create_index(
            name=PINECONE_INDEX_NAME,
            dimension=getattr(embedder, "embed_dim", 768),
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region=PINECONE_REGION),
        )

    # Connect to the Pinecone index
    index = pc.Index(name=PINECONE_INDEX_NAME)

    # Create LangChain Pinecone vectorstore instance
    # text_key is the document attribute used for text search (usually 'text' or 'content')
    vectorstore = LangchainPinecone(index=index, embedding=embedder, text_key="text")

    return vectorstore