# os and certifi will help to solve the SSL connect issue when Groq make internal https
# This sepcifically for isolated env or venv
import os
import certifi
os.environ["SSL_CERT_FILE"] = certifi.where()

from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

print(load_dotenv())
print(os.getenv("GROQ_API_KEY"))

# create one GROQ_API_KEY into ENV because Groq method will read GROQ_API_KEY from ENV
#  
# model deepseek-r1-distill-llama-70b
# pass model to Agent using Groq
agent = Agent(model=Groq(id="deepseek-r1-distill-llama-70b"), markdown=True)
def start_chat():
    text = input("ask something: ")
    text = text.strip().lower()

    if text == "exit":
        print("Bye...")
        return
    else:
        agent.print_response(f'''{text}''')
        start_chat()

start_chat()