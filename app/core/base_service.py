from typing import Any, Dict, Optional
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.sql.elements import BinaryExpression


class BaseService:
    def __init__(self, repo, model_class):
        self.repo = repo
        self.model_class = model_class
        self.db = repo.db
        
    def create(self, data: Dict):
        obj = self.model_class(**data)
        return self.repo.create(obj)
    
    def get(self, value: Any, column: InstrumentedAttribute):
        return self.repo.get(value, column)

    def get_where(self, *conditions: BinaryExpression):
        return self.repo.get_where(*conditions)

    def list_all(self):
        return self.repo.get_all()

    def update(self, value: Any, column: InstrumentedAttribute, data: Dict):
        obj = self.repo.get(value, column)
        if not obj:
            return None
        return self.repo.update(obj, data)
    
    def delete(self, value: Any, column: InstrumentedAttribute):
        return self.repo.delete(value, column)