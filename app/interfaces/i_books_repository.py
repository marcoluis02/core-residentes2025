from typing import Protocol, Any
from sqlalchemy.orm.attributes import InstrumentedAttribute
from app.models.books import Book


class IBooksRepository(Protocol):
    def create(self, obj: Book) -> Book:
        ...

    def get(self, value: Any, column: InstrumentedAttribute) -> Book | None:
        ...

    def get_where(self, *conditions: Any) -> list[Book]:
        ...

    def get_all(self) -> list[Book]:
        ...

    def update(self, obj: Book, data: dict) -> Book | None:
        ...

    def delete(self, value: Any, column: InstrumentedAttribute) -> bool:
        ...
