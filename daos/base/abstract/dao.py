from abc import ABC, abstractmethod
from typing import Type, Any, List

from daos.base.abstract.model import BaseModel


class BaseDao(ABC):
    def __init__(self, model: Type):
        self.model = model

    @abstractmethod
    def get_all(self) -> List[BaseModel]:
        pass

    @abstractmethod
    def get_by_id(self, _id: int | str) -> BaseModel | None:
        pass

    @abstractmethod
    def create(self, data: Any) -> BaseModel:
        pass

    @abstractmethod
    def update(self, data: Any) -> BaseModel:
        pass

    @abstractmethod
    def delete(self, _id: int | str) -> None:
        pass
