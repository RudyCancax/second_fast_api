from fastapi import FastAPI, Path, Query, HTTPException
from Book import Book, BookRequest

app = FastAPI()

BOOKS = [
    Book(1, "To Kill a Mockingbird", "Harper Lee", "A classic novel set in the American South during the 1930s, tackling themes of racial injustice and moral growth through the eyes of young Scout Finch.", 5, 2000),
    Book(2, "1984", "George Orwell", "A dystopian novel depicting a totalitarian regime where individuality is suppressed, and truth is manipulated, offering a stark warning about the dangers of authoritarianism.", 4, 2000),
    Book(3, "Pride and Prejudice", "Jane Austen", "A timeless romantic comedy of manners that explores themes of marriage, social class, and personal growth through the interactions of Elizabeth Bennet and Mr. Darcy.", 4, 2010),
    Book(4, "The Catcher in the Rye", "J.D. Salinger", "A coming-of-age novel following Holden Caulfield's journey of self-discovery and disillusionment as he navigates the complexities of adolescence and adulthood in post-war America.", 4, 2000),
    Book(5, "The Great Gatsby", "F. Scott Fitzgerald", "Set in the roaring twenties, this novel delves into the lavish and morally ambiguous world of Jay Gatsby, exploring themes of love, wealth, and the American Dream.", 4, 2010),
    Book(6, "To the Lighthouse", "Virginia Woolf", "A modernist masterpiece that delves into the complexities of human relationships, perception, and the passage of time, as a family navigates their emotions during a visit to a lighthouse.", 5, 2020),
    Book(7, "One Hundred Years of Solitude", "Gabriel García Márquez", "A groundbreaking work of magical realism that chronicles the multi-generational saga of the Buendía family in the fictional town of Macondo, blending myth and reality to explore themes of love, fate, and solitude.", 5, 2020),
    Book(8, "The Lord of the Rings", "J.R.R. Tolkien", "An epic high-fantasy trilogy that follows Frodo Baggins and his companions as they embark on a perilous journey to destroy the One Ring and defeat the dark lord Sauron, set in the richly imagined world of Middle-earth.", 5, 2020),
    Book(9, "Beloved", "Toni Morrison", "A haunting tale of slavery's legacy, centered around Sethe, a former slave haunted by the memories of her past, and the ghost of her deceased daughter, exploring themes of trauma, identity, and redemption.", 4, 2020),
    Book(10, "The Road", "Cormac McCarthy", "A post-apocalyptic novel following a father and his young son as they journey across a desolate landscape, struggling to survive and maintain their humanity in a world devoid of hope, exploring themes of love, survival, and the human spirit.", 4, 2022)
]


@app.get('/')
def empty_state_api_2():
    return "Hello API 2"

@app.get('/books')
def return_books():
    return BOOKS

@app.get('/books/get-by-year/')
def gets_book_by_published_year(published_year : int = Query(gt=1999, lt=2024)):
    books = []
    for book in BOOKS:
        if book.published_date == published_year:
            print(book.published_date)
            books.append(book)
    if books:
        return books;
    else:
        raise HTTPException(status_code=404, detail=f"Book with published year: {published_year}, NOT FOUND!")
    
@app.get('/books/find-by-id/{book_id}')
def find_book_by_id(book_id : int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    else:
        raise HTTPException(status_code=404, detail=f"Book with id: {book_id}, NOT FOUND!")
    
@app.post('/books/new-book')
def return_books(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(complete_book(new_book))
    return BOOKS

    
    
@app.post('/books/books-by-rating/')
def find_book_by_rate(rate : int):
    books = []
    for book in BOOKS:
        if book.rating == rate:
            books.append(book)
    if books:
        return books
    else:
        raise HTTPException(status_code=404, detail=f"Books with rate: {rate}, NOT FOUND!")
    
@app.put('/books/update-book/')
def update_book_by_id_using_put(id : int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == id:
            BOOKS[i].description = 'Labore labore sit quis laboris adipisicing ex proident veniam enim duis amet.'
            return BOOKS[i]
    else:
        raise HTTPException(status_code=404, detail=f"Books with id: {id}, NOT FOUND!")
    
@app.delete('/books/delete-book/')
def delete_book_by_id(id : int):
    bookId = None
    for i in range(len(BOOKS)):
        if BOOKS[i].id == id:
            bookId = i
    if bookId:
        BOOKS.pop(i)
        return BOOKS;
    else:
        raise HTTPException(status_code=404, detail=f"Books with id: {id}, NOT FOUND!")
        

def complete_book(book : Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 10
    return book