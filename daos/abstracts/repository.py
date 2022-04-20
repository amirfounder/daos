from abc import ABC, abstractmethod
from typing import Any, List, Generic, TypeVar

T = TypeVar('T')


class BaseRepository(Generic[T], ABC):
    def __init__(self):
        self.model = T

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
