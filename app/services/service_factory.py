from sqlalchemy.orm import Session
from app.services.carros_service import CarrosService

class ServiceFactory:
    def __init__(self, db: Session):
        self.db = db

    def carros_service(self):
        return CarrosService(self.db)
