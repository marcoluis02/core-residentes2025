from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.services.service_factory import ServiceFactory
from app.dto.albums_dto import AlbumCreateDTO, AlbumUpdateDTO, AlbumResponseDTO
from app.models.albums import Album
from typing import Optional
from fastapi import Query
from app.factories.repository_factory import  get_albums_service
router = APIRouter(prefix="/albums", tags=["Albums"])

#create, read, update, delete
@router.post("/", response_model=AlbumResponseDTO)
def create_album(data: AlbumCreateDTO, db: Session = Depends(get_db)):
    service = get_albums_service(db)
    return service.create(data.dict())

#consultas personalizadas
@router.get("/get_where", response_model=list[AlbumResponseDTO])
def buscar_albums(
    brand: Optional[str] = Query(None, description="Marca del carro"),
    year: Optional[int] = Query(None, description="Año del carro"),
    precio_min: Optional[float] = Query(None, description="Precio mínimo"),
    precio_max: Optional[float] = Query(None, description="Precio máximo"),
    db: Session = Depends(get_db)
):
    service = get_albums_service(db)

    condiciones = []
    if brand:
        condiciones.append(Album.brand == brand)
    if year:
        condiciones.append(Album.year == year)
    if precio_min is not None:
        condiciones.append(Album.price >= precio_min)
    if precio_max is not None:
        condiciones.append(Album.price <= precio_max)

    albums = service.get_where(*condiciones) if condiciones else service.list_all()

    if not albums:
        raise HTTPException(status_code=404, detail="No se encontraron albums con esos filtros")

    return albums

@router.get("/{album_id}", response_model=AlbumResponseDTO)
def get_album(album_id: int, db: Session = Depends(get_db)):
    service = get_albums_service(db)
    album = service.get(album_id, Album.id)
    if not album:
        raise HTTPException(status_code=404, detail="Album no encontrado")
    return album

@router.get("/", response_model=list[AlbumResponseDTO])
def list_albums(db: Session = Depends(get_db)):
    service = get_albums_service(db)
    return service.list_all()

@router.put("/{album_id}", response_model=AlbumResponseDTO)
def update_album(album_id: int, data: AlbumUpdateDTO, db: Session = Depends(get_db)):
    service = get_albums_service(db)
    album = service.update(album_id, Album.id, data.dict(exclude_unset=True))
    if not album:
        raise HTTPException(status_code=404, detail="Album no encontrado")
    return album

@router.delete("/{album_id}")
def delete_album(album_id: int, db: Session = Depends(get_db)):
    service = get_albums_service(db)
    deleted = service.delete(album_id, Album.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Album no encontrado")
    return {"message": "Album eliminado"}

