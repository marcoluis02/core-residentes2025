from typing import Protocol, Any
from sqlalchemy.orm.attributes import InstrumentedAttribute
from app.models.usuarios import Usuario

class IUsuariosRepository(Protocol):
    def create(self, obj: Usuario) -> Usuario:
        ...

    def get(self, value: Any, column: InstrumentedAttribute) -> Usuario | None:
        ...

    def get_where(self, *conditions: Any) -> list[Usuario]:
        ...

    def get_all(self) -> list[Usuario]:
        ...

    def update(self, obj: Usuario, data: dict) -> Usuario | None:
        ...

    def delete(self, value: Any, column: InstrumentedAttribute) -> bool:
        ...
