from app.core.basecrud import BaseCRUD
from app.models.usuarios import Usuario
from app.interfaces.i_usuarios_repository import IUsuariosRepository

class UsuariosRepository(BaseCRUD[Usuario], IUsuariosRepository):
    def __init__(self, db):
        super().__init__(Usuario, db)
