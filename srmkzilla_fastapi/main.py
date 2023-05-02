from fastapi import FastAPI, Response
from routes import test, utilities
from json import dumps

app = FastAPI()
app.include_router(test.router)

@app.get("/")
async def home():
    return Response(
        dumps({"message": "Welcome to BookStoreAPI"}),
        status_code=200,
        media_type="application/json"
    )
