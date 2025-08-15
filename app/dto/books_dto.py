from pydantic import BaseModel
from decimal import Decimal
from datetime import date


class BookCreateDTO(BaseModel):
    title: str
    author: str
    price: Decimal
    publication_date: date


class BookReadDTO(BaseModel):
    id: int
    title: str
    author: str
    price: Decimal
    publication_date: date


class BookUpdateDTO(BaseModel):
    title: str
    author: str
    price: Decimal
    publication_date: date


class BookResponseDTO(BaseModel):
    id: int
    title: str
    author: str
    price: Decimal
    publication_date: date
