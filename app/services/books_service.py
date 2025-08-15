from app.core.base_service import BaseService
from app.models.books import Book
from app.repositories.books_repository import BooksRepository
from sqlalchemy.orm import Session


class BooksService(BaseService):
    def __init__(self, repository: BooksRepository, db: Session):
        super().__init__(repository, Book)
        self.db = db
