from typing import Protocol, Any
from sqlalchemy.orm.attributes import InstrumentedAttribute
from app.models.albums import Album

class IAlbumsRepository(Protocol):
    def create(self, obj: Album) -> Album:
        ...

    def get(self, value: Any, column: InstrumentedAttribute) -> Album | None:
        ...

    def get_where(self, *conditions: Any) -> list[Album]:
        ...

    def get_all(self) -> list[Album]:
        ...

    def update(self, obj: Album, data: dict) -> Album | None:
        ...

    def delete(self, value: Any, column: InstrumentedAttribute) -> bool:
        ...
