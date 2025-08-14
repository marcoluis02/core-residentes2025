from app.core.base_service import BaseService
from app.models.albums import Album
from app.repositories.albums_repository import AlbumsRepository
from sqlalchemy.orm import Session

class AlbumsService(BaseService):
    def __init__(self, repository: AlbumsRepository, db: Session):
        super().__init__(repository, Album)
        self.db = db
    