import pymongo
import os

from dotenv import load_dotenv


load_dotenv()
client = pymongo.MongoClient(os.getenv("uri"))

db = client["work"]
collection = db["books"]

async def get_all_books():
    return collection.find()

async def get_book_by_id(id):
    return collection.find_one({"_id": id})

async def search_book(query):
    return collection.find({"$text": {"$search": query}})