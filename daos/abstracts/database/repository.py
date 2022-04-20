from abc import ABC
from typing import Generic, TypeVar

from .schema_loader import SchemaLoader
from ..repository import BaseRepository

from .config import database

T = TypeVar('T')


class BaseDBRepository(BaseRepository[T], Generic[T], ABC):
    def __init__(self, model: T):
        super().__init__(model)
        self.schema_loader = SchemaLoader(database, model)
        self.schema_loader.load()

    def create(self, **kwargs):
        return self.model.create(**kwargs)

    def get(self, identifier):
        return self.model.select(self.model).filter(id=identifier)

    def get_all(self):
        return self.model.select(self.model)

    def update(self, instance):
        return self.model.update(self.model)

    def save(self, instance):
        return instance.save()

    def delete(self, identifier):
        return self.model.delete(self.model)
