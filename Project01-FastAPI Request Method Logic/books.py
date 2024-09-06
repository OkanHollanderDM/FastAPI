from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {"name": "Harry Potter", "author": "J.K. Rowling", "category": "fantasy"},
    {"name": "Lord of the Rings", "author": "J.R.R. Tolkien", "category": "fantasy"},
    {"name": "The Alchemist", "author": "Paulo Coelho", "category": "adventure"},
    {"name": "The Da Vinci Code", "author": "Dan Brown", "category": "mystery"},
    {"name": "The Little Prince", "author": "Antoine de Saint-Exupéry", "category": "fantasy"},
    {"name": "The Hobbit", "author": "J.R.R. Tolkien", "category": "fantasy"},
    {"name": "And Then There Were None", "author": "Agatha Christie", "category": "mystery"},
    {"name": "Dream of the Red Chamber", "author": "Cao Xueqin", "category": "romance"},
    {"name": "The Lion, the Witch and the Wardrobe", "author": "C.S. Lewis", "category": "fantasy"},
    {"name": "She: A History of Adventure", "author": "H. Rider Haggard", "category": "adventure"},
    {"name": "The Adventures of Sherlock Holmes", "author": "Arthur Conan Doyle", "category": "mystery"},
    {"name": "The Godfather", "author": "Mario Puzo", "category": "crime"},
    {"name": "The Catcher in the Rye", "author": "J.D. Salinger", "category": "fiction"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('name').casefold() == book_title.casefold():
            return book

@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/byauthor/")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold() and \
                book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book=Body(...)):
    BOOKS.append(new_book)
    return new_book

@app.put("/books/update_book/{book_title}")
async def update_book(book_title: str, updated_book=Body(...)):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("name").casefold() == book_title.casefold():
            BOOKS[i] = updated_book
            return updated_book
    return {"error": "Book not found"}

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("name").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break