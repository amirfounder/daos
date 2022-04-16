from datetime import datetime
from typing import Dict, Type, List

from pgsql_repository.core import Metadata
from pgsql_repository.factory.random_type_generators import (
    RandomTypeGenerator,
    RandomDatetime,
    RandomFloat,
    RandomInt,
    RandomStr
)
from pgsql_repository.model.model import BaseModel


class BaseRandomModelFactory:
    type_mappings: Dict[Type, RandomTypeGenerator] = {
        str: RandomStr(),
        int: RandomInt(),
        float: RandomFloat(),
        datetime: RandomDatetime()
    }
    
    def __init__(self, model: Type[BaseModel], metadata: Metadata = Metadata,):
        self.model = model
        self.metadata = metadata
    
    def register_generator(self, _type: Type, generator: Type[RandomTypeGenerator], **kwargs):
        self.type_mappings[_type] = generator(**kwargs)

    def create_many(self, count: int) -> List[BaseModel]:
        return [self.create() for _ in range(count)]

    def create(self) -> BaseModel:
        kwargs = {}
        for c in self.model.get_columns().values():
            if not c.primary_key:
                kwargs[c.name] = self.type_mappings.get(c.type.python_type).get()
        return self.model(**kwargs)
