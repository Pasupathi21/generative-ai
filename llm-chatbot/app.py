from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

# set title
st.title("PASUPA(🔥)'s Chat Bot")

# get input text values
input_text = st.text_input("Search to explore new things")

# create prompt template
template = ChatPromptTemplate.from_messages([
    ("system", "Your name is Gandhi Babu"),
    ("user", "user query: {query}")
])

# initialize llm model
llm = Ollama(model="phi3:mini")

# output parser initialize
parser = StrOutputParser()

# finally chaining the template, llm and parser
chain = template|llm|parser

# pass the input text to stramlit 
if input_text.strip():
    # invoke the chain and pass to streamlit instance
    st.write(chain.invoke({"query": input_text}))

