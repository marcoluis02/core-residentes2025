from app.core.base_service import BaseService
from app.models.usuarios import Usuario
from app.repositories.usuarios_repository import UsuariosRepository
from sqlalchemy.orm import Session

class UsuariosService(BaseService):
    def __init__(self, repository: UsuariosRepository, db: Session):
        super().__init__(repository, Usuario)
        self.db = db
    