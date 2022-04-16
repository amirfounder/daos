import string
import random
from typing import TypeVar, Generic, Generator, Dict, Any, Type, Callable

from pgsql_repository.core import Metadata

T = TypeVar('T')


class RandomByType:
    def __init__(self):
        super().__init__()
        self.map: Dict[Type, Callable] = {
            str: self._rand_str,
            int: self._rand_int,
            float: self._rand_float,
        }

    @staticmethod
    def _rand_str(
            include_upper: bool = True,
            include_lower: bool = True,
            include_numbers: bool = True
    ):
        pool = ''
        if include_upper:
            pool += string.ascii_uppercase
        if include_lower:
            pool += string.ascii_lowercase
        if include_numbers:
            pool += string.digits
        return pool[random.randint(0, len(pool) - 1)]

    @staticmethod
    def _rand_int(minimum: int = 0, maximum: int = 100):
        return random.randint(minimum, maximum)

    @staticmethod
    def _rand_float(minimum: float = 0, maximum: float = 100.0, decimal_places: int = 1):
        return round(random.uniform(minimum, maximum), decimal_places)

    def get(self, _type: Type, **kwargs):
        if rand := self.map.get(_type):
            return rand(**kwargs)


class Factory(Generic[T]):
    def __init__(
            self,
            model: Type[T],
            metadata: Metadata = Metadata,
            random_by_type: RandomByType = RandomByType()
    ):
        self.model: Type[T] = model
        self.metadata = metadata
        self.random_by_type = random_by_type

    def _create_model_column_value_map(self, type_map: Dict[str, Any]):
        pass

    def _create_model_column_type_map(self):
        return {n: c.type for n, c in self.model.get_columns().items()}

    def create_many(self, count: int) -> Generator[T, None, None]:
        for i in range(count):
            yield self.create()

    def create(self) -> T:
        kwargs = {}
        for c in self.model.get_columns().values():
            if not c.primary_key:
                kwargs[c.name] = self.random_by_type.get(c.type)
        return self.model(**kwargs)
