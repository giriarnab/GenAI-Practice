import os
os.environ['USER_AGENT'] = 'myagent'

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


mymodel = ChatOllama(model="mistral",
                     temperature=0)

#1. split data into chunks
urls = [
        "https://docs.oracle.com/cd/F25688_01/oipa_activityprocessing/Content/OIPA%20Activity%20Processing/Shared%20Rules%20Engine.htm",
        "https://docs.oracle.com/cd/F25688_01/oipa_activityprocessing/Content/OIPA%20Activity%20Processing/Understanding%20Activities.htm",
        ]
docs = [WebBaseLoader(url).load() for url in urls]
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

question = "What are different types of activities in OIPA"
#3. Before RAG 
print("Before RAG \n")
before_rag_template = question
before_rag_prompt = ChatPromptTemplate.from_template(before_rag_template)
before_rag_chain = before_rag_prompt | mymodel | StrOutputParser()
print(before_rag_chain.invoke({"topic":"Ollama"}))


#4. After RAG
print("After RAG \n")
after_rag_template = """Answer question based on : {context} Question :{question}"""
after_rag_prompt = ChatPromptTemplate.from_template(after_rag_template)
after_rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | after_rag_prompt
    | mymodel
    | StrOutputParser()
)

print(after_rag_chain.invoke(question))