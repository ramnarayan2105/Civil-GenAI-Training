import os
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

#prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{Question}")
    ]
)

#streamlit template
st.title("MYGPT")
input_text=st.text_input("Ask your question")

#ollama model
llm= OllamaLLM(model="gemma2:2b")

output_parser=StrOutputParser()
chain=prompt|llm|output_parser
st.write(chain.invoke({"Question":input_text}))