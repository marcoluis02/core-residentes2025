from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.services.service_factory import ServiceFactory
from app.dto.usuarios_dto import UsuarioCreateDTO, UsuarioUpdateDTO, UsuarioResponseDTO
from app.models.usuarios import Usuario
from typing import Optional
from fastapi import Query
from app.factories.repository_factory import  get_usuarios_service
router = APIRouter(prefix="/usuarios", tags=["usuarios"])

#create, read, update, delete
@router.post("/", response_model=UsuarioResponseDTO)
def create_usuario(data: UsuarioCreateDTO, db: Session = Depends(get_db)):
    service = get_usuarios_service(db)
    return service.create(data.dict())

#consultas personalizadas
@router.get("/get_where", response_model=list[UsuarioResponseDTO])
def buscar_usuarios(
    nombre: Optional[str] = Query(None, description="Nombre del usuario"),
    email: Optional[str] = Query(None, description="Email del usuario"),
    edad_min: Optional[int] = Query(None, description="Edad mínima"),
    edad_max: Optional[int] = Query(None, description="Edad máxima"),
    db: Session = Depends(get_db)
):
    service = get_usuarios_service(db)

    condiciones = []
    if nombre:
        condiciones.append(Usuario.nombre == nombre)
    if email:
        condiciones.append(Usuario.email == email)
    if edad_min is not None:
        condiciones.append(Usuario.edad >= edad_min)
    if edad_max is not None:
        condiciones.append(Usuario.edad <= edad_max)

    usuarios = service.get_where(*condiciones) if condiciones else service.list_all()

    if not usuarios:
        raise HTTPException(status_code=404, detail="No se encontraron usuarios con esos filtros")

    return usuarios

@router.get("/{usuario_id}", response_model=UsuarioResponseDTO)
def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    service = get_usuarios_service(db)
    usuario = service.get(usuario_id, Usuario.id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.get("/", response_model=list[UsuarioResponseDTO])
def list_usuarios(db: Session = Depends(get_db)):
    service = get_usuarios_service(db)
    return service.list_all()

@router.put("/{usuario_id}", response_model=UsuarioResponseDTO)
def update_usuario(usuario_id: int, data: UsuarioUpdateDTO, db: Session = Depends(get_db)):
    service = get_usuarios_service(db)
    usuario = service.update(usuario_id, Usuario.id, data.dict(exclude_unset=True))
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.delete("/{usuario_id}")
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    service = get_usuarios_service(db)
    deleted = service.delete(usuario_id, Usuario.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"message": "Usuario eliminado"}

