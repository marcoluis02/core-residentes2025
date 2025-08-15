from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.services.service_factory import ServiceFactory
from app.dto.clientes_dto import ClienteCreateDTO, ClienteUpdateDTO, ClienteResponseDTO
from app.models.clientes import Cliente
from app.factories.repository_factory import get_clientes_service
from typing import Optional

router = APIRouter(prefix="/clientes", tags=["Clientes"])

# --- Create ---
@router.post("/", response_model=ClienteResponseDTO)
def create_cliente(data: ClienteCreateDTO, db: Session = Depends(get_db)):
    service = get_clientes_service(db)
    return service.create(data.dict())

# --- Read with filters ---
@router.get("/get_where", response_model=list[ClienteResponseDTO])
def buscar_clientes(
    nombre: Optional[str] = Query(None, description="Nombre del cliente"),
    apellido: Optional[str] = Query(None, description="Apellido del cliente"),
    db: Session = Depends(get_db)
):
    service = get_clientes_service(db)

    condiciones = []
    if nombre:
        condiciones.append(Cliente.nombre == nombre)
    if apellido:
        condiciones.append(Cliente.apellido == apellido)

    clientes = service.get_where(*condiciones) if condiciones else service.list_all()

    if not clientes:
        raise HTTPException(status_code=404, detail="No se encontraron clientes con esos filtros")

    return clientes

# --- Read by ID ---
@router.get("/{cliente_id}", response_model=ClienteResponseDTO)
def get_cliente(cliente_id: int, db: Session = Depends(get_db)):
    service = get_clientes_service(db)
    cliente = service.get(cliente_id, Cliente.id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

# --- List all ---
@router.get("/", response_model=list[ClienteResponseDTO])
def list_clientes(db: Session = Depends(get_db)):
    service = get_clientes_service(db)
    return service.list_all()

# --- Update ---
@router.put("/{cliente_id}", response_model=ClienteResponseDTO)
def update_cliente(cliente_id: int, data: ClienteUpdateDTO, db: Session = Depends(get_db)):
    service = get_clientes_service(db)
    cliente = service.update(cliente_id, Cliente.id, data.dict(exclude_unset=True))
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

# --- Delete ---
@router.delete("/{cliente_id}")
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    service = get_clientes_service(db)
    deleted = service.delete(cliente_id, Cliente.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return {"message": "Cliente eliminado"}
