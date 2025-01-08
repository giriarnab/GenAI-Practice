import os
os.environ['USER_AGENT'] = 'myagent'

import gradio as gr
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
# from langchain_community import embeddings
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from bs4 import BeautifulSoup

def process (urls, question):

    mymodel = ChatOllama(model="mistral",
                        temperature=0)

    #1. split data into chunks
    url_list = urls.split("\n")
    docs = [WebBaseLoader(url).load() for url in url_list]
    docs_lists = [item for sublist in docs for item in sublist]
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=7500, chunk_overlap=100)
    doc_splits = text_splitter.split_documents(docs_lists)

    #2.Convert documents into Embeddings
    vectorstore =Chroma.from_documents(
        documents=doc_splits,
        collection_name="rag-chroma",
        embedding=OllamaEmbeddings(model='nomic-embed-text')
    )

    retriever = vectorstore.as_retriever()

    #4. After RAG
    print("Running RAG ... \n")
    after_rag_template = """Answer question based on : {context} Question :{question}"""
    after_rag_prompt = ChatPromptTemplate.from_template(after_rag_template)
    after_rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | after_rag_prompt
        | mymodel
        | StrOutputParser()
    )

    return after_rag_chain.invoke(question)

#Define Gradio Interface
ui = gr.Interface(fn=process,
                    inputs=[gr.TextArea(label="Enter URLs in seperate lines", ), gr.Textbox(label="Enter a question")],
                    outputs="text",
                    title="Gen AI Interface with Ollama",
                    description="Enter URLs and Questions")

ui.launch(share=True)