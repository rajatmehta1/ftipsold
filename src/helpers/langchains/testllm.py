import os

os.environ["OPENAI_API_KEY"] = "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"

from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9,model_name="gpt-3.5-turbo-0613")



text = "How should i increase my productivity many times"
print(llm(text))