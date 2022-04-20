from abc import ABC
from typing import Generic, TypeVar

from ..repository import BaseRepository

T = TypeVar('T')


class BaseDBRepository(BaseRepository[T], Generic[T], ABC):
    def get(self, identifier):
        return self.model.select(self.model).filter(id=identifier)

    def get_all(self):
        return self.model.select(self.model)

    def update(self, instance):
        return self.model.update(self.model)

    def save(self, instance):
        return self.model.insert(self.model)

    def delete(self, identifier):
        return self.model.delete(self.model)
