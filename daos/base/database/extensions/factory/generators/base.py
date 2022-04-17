from abc import ABC, abstractmethod
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from daos.base.database.extensions.factory.factory import BaseModelFactory


class RandomGenerator(ABC):
    @abstractmethod
    def __init__(self, **kwargs): ...

    @abstractmethod
    def get(self) -> Any: ...
