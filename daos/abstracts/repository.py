from abc import ABC, abstractmethod
from typing import Any, List, Generic, TypeVar

from .model import BaseModel

T = TypeVar('T', bound=BaseModel)


class BaseRepository(Generic[T], ABC):
    def __init__(self, model: T):
        self.model = model

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def get(self, identifier: Any) -> T | None:
        pass

    @abstractmethod
    def save(self, instance: Any) -> T:
        pass

    @abstractmethod
    def update(self, instance: Any) -> T:
        pass

    @abstractmethod
    def delete(self, identifier: int | str) -> None:
        pass
