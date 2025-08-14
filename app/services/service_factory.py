from sqlalchemy.orm import Session
from app.services.albums_service import AlbumService

class ServiceFactory:
    def __init__(self, db: Session):
        self.db = db

    def carros_service(self):
        return AlbumsService(self.db)
