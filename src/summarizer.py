from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

def get_summarizer_chain(vectorstore):
    summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")
    llm = HuggingFacePipeline(pipeline=summarization_pipeline)
    return RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())