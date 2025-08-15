from sqlalchemy.orm import Session
from app.services.clientes_service import ClientesService
from app.repositories.clientes_repository import ClientesRepository

class ServiceFactory:
    def __init__(self, db: Session):
        self.db = db

    def clientes_service(self):
        repository = ClientesRepository(self.db)
        return ClientesService(repository, self.db)

