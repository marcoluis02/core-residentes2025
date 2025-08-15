from pydantic import BaseModel
from datetime import date
from typing import Optional

class ClienteCreateDTO(BaseModel):
    nombre: str
    apellido: Optional[str] = None
    telefono: Optional[str] = None
    fecha_nacimiento: Optional[date] = None

class ClienteReadDTO(BaseModel):
    id: int
    nombre: str
    apellido: Optional[str] = None
    telefono: Optional[str] = None
    fecha_nacimiento: Optional[date] = None

class ClienteUpdateDTO(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    telefono: Optional[str] = None
    fecha_nacimiento: Optional[date] = None

class ClienteResponseDTO(BaseModel):
    id: int
    nombre: str
    apellido: Optional[str] = None
    telefono: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
