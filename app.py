import streamlit as st
import tempfile
import os

from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
from langchain.docstore.document import Document

from src.main import build_vectorstore, query_vectorstore

st.set_page_config(page_title="Knowledge Chat", layout="wide")
st.title("📚 Knowledge Base Q&A")

if "uploaded_docs" not in st.session_state:
    st.session_state.uploaded_docs = []
if "vectorstore_ready" not in st.session_state:
    st.session_state.vectorstore_ready = False
if "history" not in st.session_state:
    st.session_state.history = []

# Upload section
uploaded_files = st.file_uploader(
    "Upload your documents (PDF or TXT)", type=["pdf", "txt"], accept_multiple_files=True
)

if uploaded_files:
    all_docs = []
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp_file:
            tmp_file.write(file.read())
            tmp_file_path = tmp_file.name

        if file_ext == ".pdf":
            loader = PyMuPDFLoader(tmp_file_path)
        elif file_ext == ".txt":
            loader = TextLoader(tmp_file_path)
        else:
            st.warning(f"Unsupported file format: {file.name}")
            continue

        docs = loader.load()
        all_docs.extend(docs)
        os.remove(tmp_file_path)

    st.session_state.uploaded_docs = all_docs
    st.success(f"{len(all_docs)} document pages loaded.")

if st.button("📌 Build Vectorstore"):
    if st.session_state.uploaded_docs:
        build_vectorstore(st.session_state.uploaded_docs)
        st.session_state.vectorstore_ready = True
        st.success("✅ Vectorstore is ready! You can now ask questions.")
    else:
        st.warning("Please upload documents first.")

# Q&A section
st.subheader("💬 Ask a question:")
query = st.text_input("Your question here...")

if st.button("➡️ Send"):
    if not st.session_state.vectorstore_ready:
        st.warning("Please build the vectorstore first.")
    elif query.strip() == "":
        st.warning("Enter a valid question.")
    else:
        with st.spinner("Thinking..."):
            answer = query_vectorstore(query.strip())
            st.session_state.history.append({"user": query, "bot": answer})

# Chat history display
for chat in reversed(st.session_state.history):
    st.markdown(f"**🧑 You:** {chat['user']}")
    st.markdown(f"**🤖 Bot:** {chat['bot']}")
    st.markdown("---")