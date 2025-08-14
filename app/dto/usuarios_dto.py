from pydantic import BaseModel


class UsuarioCreateDTO(BaseModel):
    nombre: str
    email: str
    edad: int

class UsuarioReadDTO(BaseModel):
    id: int
    nombre: str
    email: str
    edad: int

class UsuarioUpdateDTO(BaseModel):
    nombre: str
    email: str
    edad: int

class UsuarioResponseDTO(BaseModel):
    id: int
    nombre: str
    email: str
    edad: int