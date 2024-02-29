import os
from langchain.llms import OpenAI
from dotenv import load_dotenv

class ChainHelper:
    
    def __init__(self):
        load_dotenv()  # take environment variables from .env.
        api_key = os.getenv("OPENAI_API_KEY")
        self.llm = OpenAI(temperature=0.9,model_name="gpt-3.5-turbo-0613")


    def reply(self, question):
        return self.llm(question)