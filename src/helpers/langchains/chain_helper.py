import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

class ChainHelper:
    
    def __init__(self):
        load_dotenv()  # take environment variables from .env.
        api_key = os.getenv("OPENAI_API_KEY")
        self.llm = ChatOpenAI(temperature=0.9,openai_api_key=api_key)


    def reply(self, question):
        return self.llm.invoke(question)