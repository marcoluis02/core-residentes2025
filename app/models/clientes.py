from sqlalchemy import Column, Integer, String, Date
from app.core.db import Base  # conserva tu estructura de proyecto

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100))
    telefono = Column(String(20))
    fecha_nacimiento = Column(Date)
