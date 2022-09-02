from fastapi import FastAPI
import uvicorn

app = FastAPI(debug=True)
messages: dict = {}

@app.get("/tweets")
async def tweets():
    return messages

uvicorn.run(app, host="127.0.0.1", port=8080)