from abc import ABC, abstractmethod
from typing import Type, Dict

from daos.base.abstract.model import BaseModel


class BaseDao(ABC):
    def __init__(self, model: Type[BaseModel], permissions: Dict[str, bool]):
        self.model = model
        self.permissions = permissions

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, _id: int | str):
        pass

    @abstractmethod
    def create(self, entity: BaseModel):
        pass

    @abstractmethod
    def update(self, entity: BaseModel):
        pass

    @abstractmethod
    def delete(self, _id: int | str):
        pass
