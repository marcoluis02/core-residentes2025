import os
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.interfaces.i_usuarios_repository import IUsuariosRepository
from app.repositories.usuarios_repository import UsuariosRepository
from app.services.usuarios_service import UsuariosRepository, UsuariosService

#Cuando se agreguen más repositorios, se puede usar este factory method para elegir entre ellos
def factory_method(func):
    use_Dynamo = os.getenv("USE_DYNAMO", "false").lower() == "true"
    db_engine = os.getenv("DB_ENGINE", "POSTGRES").upper()
    if use_Dynamo or db_engine == "DYNAMODB":
        return None  # Placeholder for DynamoDB repository if implemented
    if func is None:
        raise ValueError("Invalid database session provided for Postgres repository.")
def set_search_schema(db: Session | None):
    if db is None:
        raise ValueError("Invalid database session provided for Postgres repository.")
    print(f"Setting search path to DB_SCHEMA") #DB_SCHEMA is set in .env
    db.execute(text(f"SET search_path TO DB_SCHEMA")) #DB_SCHEMA is set in .env

def get_usuarios_repository(db: Session) -> IUsuariosRepository:
    #se podría agregar lógica para elegir entre diferentes repositorios
    return UsuariosRepository(db)

def get_usuarios_service(db: Session) -> UsuariosService:
    repository = get_usuarios_repository(db)
    return UsuariosService(repository, db)