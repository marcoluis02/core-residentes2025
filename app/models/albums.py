from sqlalchemy import Column, Integer, String
from app.core.db import Base

class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    año = Column(Integer, nullable=False)