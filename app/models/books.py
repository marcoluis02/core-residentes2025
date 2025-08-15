from sqlalchemy import Column, Integer, String, Numeric, Date
from app.core.db import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    publication_date = Column(Date, nullable=False)
