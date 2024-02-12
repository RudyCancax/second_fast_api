from typing import Optional
from pydantic import BaseModel, Field
class Book:
    id    : int
    title : str
    author: str
    description:str
    rating: int
    published_date: int
    
    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date
        
class BookRequest(BaseModel):
    id    : Optional[int] = None
    title : str = Field(min_length=1, max_length=50)
    author: str
    description:str
    rating: int
    published_date: int
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Any book title",
                "author": "Books's author",
                "description": "A brieve description of book",
                "rating": 5,
                "published_date": 2020
            }
        }