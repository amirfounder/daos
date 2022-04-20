from abc import ABC, abstractmethod
from typing import Type, Any, List, Generic, TypeVar

T = TypeVar('T')


class BaseRepository(Generic[T], ABC):
    def __init__(self, model: Type):
        self.model = model

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def get_by_id(self, _id: int | str) -> T | None:
        pass

    @abstractmethod
    def save(self, data: Any) -> T:
        pass

    @abstractmethod
    def update(self, data: Any) -> T:
        pass

    @abstractmethod
    def delete(self, _id: int | str) -> None:
        pass
