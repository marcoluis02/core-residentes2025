from pydantic import BaseModel


class AlbumCreateDTO(BaseModel):
    nombre: str
    autor: str
    año: int

class AlbumReadDTO(BaseModel):
    id: int
    nombre: str
    autor: str
    año: int

class AlbumUpdateDTO(BaseModel):
    nombre: str
    autor: str
    año: int
    
class AlbumResponseDTO(BaseModel):
    id: int
    nombre: str
    autor: str
    año: int