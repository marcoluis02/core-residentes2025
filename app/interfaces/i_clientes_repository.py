from typing import Protocol, Any
from sqlalchemy.orm.attributes import InstrumentedAttribute
from app.models.clientes import Cliente  # cambiamos la importación al nuevo modelo

class IClientesRepository(Protocol):
    def create(self, obj: Cliente) -> Cliente:
        ...

    def get(self, value: Any, column: InstrumentedAttribute) -> Cliente | None:
        ...

    def get_where(self, *conditions: Any) -> list[Cliente]:
        ...

    def get_all(self) -> list[Cliente]:
        ...

    def update(self, obj: Cliente, data: dict) -> Cliente | None:
        ...

    def delete(self, value: Any, column: InstrumentedAttribute) -> bool:
        ...

