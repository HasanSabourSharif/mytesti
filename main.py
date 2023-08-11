from fastapi import FastAPI

app = FastAPI()

@app.post("/question")
async def create_item(question:str):
    return {'quesion': question, "answer": question}
