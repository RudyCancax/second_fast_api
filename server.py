from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = []

@app.get('/books')
def return_books():
    return BOOKS