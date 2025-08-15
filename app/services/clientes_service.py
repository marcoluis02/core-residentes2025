from app.core.base_service import BaseService
from app.models.clientes import Cliente
from app.repositories.clientes_repository import ClientesRepository
from sqlalchemy.orm import Session

class ClientesService(BaseService):
    def __init__(self, repository: ClientesRepository, db: Session):
        super().__init__(repository, Cliente)
        self.db = db
