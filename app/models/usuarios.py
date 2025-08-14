from sqlalchemy import Column, Integer, String
from app.core.db import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)
