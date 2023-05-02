from fastapi import FastAPI, Response
from json import dumps

app = FastAPI()

@app.get("/")
def home():
    return Response(
        dumps({"message": "Hello World"}),
        status_code=200,
        media_type="application/json"
    )