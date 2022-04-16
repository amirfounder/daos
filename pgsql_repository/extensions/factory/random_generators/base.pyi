from abc import ABC, abstractmethod
from typing import Any


class RandomGenerator(ABC):
    @abstractmethod
    def __init__(self, **kwargs): ...

    @abstractmethod
    def get(self) -> Any: ...
