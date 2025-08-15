from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.models.books import Book
from app.dto.books_dto import BookResponseDTO, BookCreateDTO, BookUpdateDTO
from typing import Optional
from app.factories.repository_factory import get_books_service
from app.core.db import get_db
from datetime import date

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/", response_model=BookResponseDTO)
def create_book(data: BookCreateDTO, db: Session = Depends(get_db)):
    service = get_books_service(db)
    return service.create(data.dict())


@router.get("/", response_model=list[BookResponseDTO])
def list_books(db: Session = Depends(get_db)):
    service = get_books_service(db)
    return service.list_all()


@router.get("/get_where", response_model=list[BookResponseDTO])
def find_books(
    title: Optional[str] = Query(None, description="book title"),
    author: Optional[str] = Query(None, description="book author"),
    price_min: Optional[float] = Query(None, description="book price min"),
    price_max: Optional[float] = Query(None, description="book price max"),
    publication_date_min: Optional[date] = Query(
        None, description="Publication date from"),
    publication_date_max: Optional[date] = Query(
        None, description="Publication date to"),
    db: Session = Depends(get_db)
):
    service = get_books_service(db)

    conditions = []

    if title:
        conditions.append(Book.title.ilike(f"%{title}%"))

    if author:
        conditions.append(Book.author.ilike(f"%{author}%"))

    if publication_date_min is not None:
        conditions.append(Book.publication_date >= publication_date_min)

    if publication_date_max is not None:
        conditions.append(Book.publication_date <= publication_date_max)

    if price_min is not None:
        conditions.append(Book.price >= price_min)

    if price_max is not None:
        conditions.append(Book.price <= price_max)

    books = service.get_where(
        *conditions) if conditions else service.list_all()

    if not books:
        raise HTTPException(status_code=404, detail="No books found!")

    return books


@router.get("/{book_id}", response_model=BookResponseDTO)
def get_book(book_id: int, db: Session = Depends(get_db)):
    service = get_books_service(db)
    book = service.get(book_id, Book.id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found!")
    return book


@router.put("/{book_id}", response_model=BookResponseDTO)
def update_book(book_id: int, data: BookUpdateDTO, db: Session = Depends(get_db)):
    service = get_books_service(db)
    book = service.update(book_id, Book.id, data.dict(exclude_unset=True))
    if not book:
        raise HTTPException(status_code=404, detail="Book not found!")
    return book


@router.delete("/{book_id}")
def delete_book(book_id, db: Session = Depends(get_db)):
    service = get_books_service(db)
    deleted = service.delete(book_id, Book.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found!")
    return {"message": "Successfully deleted book!"}
