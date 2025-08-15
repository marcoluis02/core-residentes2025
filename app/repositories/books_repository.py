from app.core.basecrud import BaseCRUD
from app.models.books import Book
from app.interfaces.i_books_repository import IBooksRepository


class BooksRepository(BaseCRUD[Book], IBooksRepository):
    def __init__(self, db):
        super().__init__(Book, db)
