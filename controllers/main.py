from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "Hello from fast api"}

@app.get("/question/")
async def input(q: str = None):
    return {"message": "Hello from fast api"}

