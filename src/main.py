from .config import DOCS_PATH
from .loader import load_and_split_docs
from .embedder import get_embedder
from .vector_store import get_vector_store
from .summarizer import get_summarizer_chain

def run_pipeline():
    print("🔍 Loading documents...")
    docs = load_and_split_docs(DOCS_PATH)

    print("📐 Generating embeddings...")
    embedder = get_embedder()

    print("📌 Connecting to Pinecone...")
    vectorstore = get_vector_store(embedder)

    print("📤 Adding documents to Pinecone...")
    vectorstore.add_documents(docs)

    print("🧠 Initializing summarizer...")
    qa_chain = get_summarizer_chain(vectorstore)

    query = input("❓ Ask something about your documents: ")
    answer = qa_chain.run(query)
    print("\n💬 Summary:\n", answer)

if __name__ == "__main__":
    run_pipeline()

vectorstore = None  # global variable to hold your vectorstore

def build_vectorstore(docs):
    global vectorstore
    embedder = get_embedder()  # Your embedder setup
    vectorstore = get_vector_store(embedder)  # Your vectorstore setup
    vectorstore.add_documents(docs)

def query_vectorstore(query):
    if vectorstore is None:
        return "Upload documents first!"
    return vectorstore.similarity_search(query)