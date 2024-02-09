from pydantic import BaseModel, Field
class Book:
    id    : int
    title : str
    author: str
    description:str
    rating: int
    
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        
class BookRequest(BaseModel):
    id    : int = Field(min_length=2)
    title : str
    author: str
    description:str
    rating: int