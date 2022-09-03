from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class Message(BaseModel):
    author: str
    message: str

app = FastAPI(debug=True)
messages: dict = {}

@app.get("/tweets")
async def tweets():
    return messages

@app.post("/tweet")
async def tweet(message: Message):
    messages[message.author] = message.message
    return "Done"

uvicorn.run(app, host="127.0.0.1", port=8080)