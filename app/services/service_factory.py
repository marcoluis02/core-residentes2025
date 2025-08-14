from sqlalchemy.orm import Session
from app.services.usuarios_service import UsuariosService

class ServiceFactory:
    def __init__(self, db: Session):
        self.db = db

    def usuarios_service(self):
        return UsuariosService(self.db)
