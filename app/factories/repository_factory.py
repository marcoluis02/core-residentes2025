import os
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.interfaces.i_carros_repository import ICarrosRepository
from app.interfaces.i_books_repository import IBooksRepository
from app.repositories.carros_repository import CarrosRepository
from app.repositories.books_repository import BooksRepository
from app.services.carros_service import CarrosService
from app.services.books_service import BooksService

# Cuando se agreguen más repositorios, se puede usar este factory method para elegir entre ellos


def factory_method(func):
    use_Dynamo = os.getenv("USE_DYNAMO", "false").lower() == "true"
    db_engine = os.getenv("DB_ENGINE", "POSTGRES").upper()
    if use_Dynamo or db_engine == "DYNAMODB":
        return None  # Placeholder for DynamoDB repository if implemented
    if func is None:
        raise ValueError(
            "Invalid database session provided for Postgres repository.")


def set_search_schema(db: Session | None):
    if db is None:
        raise ValueError(
            "Invalid database session provided for Postgres repository.")
    print(f"Setting search path to DB_SCHEMA")  # DB_SCHEMA is set in .env
    # DB_SCHEMA is set in .env
    db.execute(text(f"SET search_path TO DB_SCHEMA"))


def get_carros_repository(db: Session) -> ICarrosRepository:
    # se podría agregar lógica para elegir entre diferentes repositorios
    return CarrosRepository(db)


def get_carros_service(db: Session) -> CarrosService:
    repository = get_carros_repository(db)
    return CarrosService(repository, db)


def get_books_repository(db: Session) -> IBooksRepository:
    return BooksRepository(db)


def get_books_service(db: Session) -> BooksService:
    repository = get_books_repository(db)
    return BooksService(repository, db)
