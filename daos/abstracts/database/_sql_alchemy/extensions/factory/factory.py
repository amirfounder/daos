from datetime import datetime
from typing import Dict, Type, List, Generic, TypeVar

from sqlalchemy import Column

from daos.base.database._sql_alchemy.utils import MetaData
from daos.base.database._sql_alchemy.extensions.factory.generators import (
    RandomGenerator,
    RandomDatetimeGenerator,
    RandomFloatGenerator,
    RandomIntGenerator,
    RandomStrGenerator,
    RandomBoolGenerator
)

T = TypeVar('T')


class BaseModelFactory(Generic[T]):
    generator_map: Dict[Column | Type, RandomGenerator] = {
        str: RandomStrGenerator(),
        int: RandomIntGenerator(),
        bool: RandomBoolGenerator(),
        float: RandomFloatGenerator(),
        datetime: RandomDatetimeGenerator()
    }
    
    def __init__(self, model: Type[T], metadata: MetaData = MetaData,):
        self.model = model
        self.metadata = metadata
        self.current_build = {}
    
    def register_generator(self, key: Column | Type, generator_cls: Type[RandomGenerator], **kwargs):
        generator = generator_cls(**kwargs)
        generator.factory = self

        self.generator_map[key] = generator

    def create_many(self, count: int) -> List[T]:
        return [self.create() for _ in range(count)]

    def create(self) -> T:
        for c in self.model.get_columns().values():
            if not c.primary_key:
                key = c if c in self.generator_map else c.type.python_type
                if key not in self.generator_map:
                    raise Exception(f'Generator not registered under key : {key}')
                self.current_build[c.name] = self.generator_map[key].get()
        return self.model(**self.current_build)
