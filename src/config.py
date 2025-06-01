import os

# Pinecone configuration
PINECONE_API_KEY = "pcsk_qDcxm_5MWGtm1wYNMNdbtGnx2fEBENN6D2PJtLYj24ojRQa7VmqT56BR27KRg6F5aetV4"
PINECONE_INDEX_NAME = "knowledge-base"
PINECONE_HOST = "https://knowledge-base-q2dp2fp.svc.aped-4627-b74a.pinecone.io"

# Documents folder
DOCS_PATH = os.path.join(os.path.dirname(__file__), "..", "docs")