from app.core.basecrud import BaseCRUD
from app.models.albums import Album
from app.interfaces.i_albums_repository import IAlbumsRepository

class AlbumsRepository(BaseCRUD[Album], IAlbumsRepository):
    def __init__(self, db):
        super().__init__(Album, db)
