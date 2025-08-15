from app.core.basecrud import BaseCRUD
from app.models.clientes import Cliente
from app.interfaces.i_clientes_repository import IClientesRepository

class ClientesRepository(BaseCRUD[Cliente], IClientesRepository):
    def __init__(self, db):
        super().__init__(Cliente, db)
        self.db = db
