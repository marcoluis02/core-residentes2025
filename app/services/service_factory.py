from sqlalchemy.orm import Session
from app.services.albums_service import AlbumsService

class ServiceFactory:
    def __init__(self, db: Session):
        self.db = db

    def albums_service(self):
        return AlbumsService(self.db)
