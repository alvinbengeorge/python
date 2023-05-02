from pydantic import BaseModel

class BookSchema(BaseModel):
    name: str
    author: str
    price: float
    pages: int
    rating: float
    coverPhoto: str
    visits: int
    description: str
    noOfCopies: int

class UpdateBookRating(BaseModel):
    rating: float

class UpdateBookCopies(BaseModel):
    noOfCopies: int