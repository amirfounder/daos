from datetime import datetime
from typing import Dict, Type, List

from sqlalchemy import Column

from daos.base.database.utils import Metadata
from daos.base.database.extensions.factory.generators.types import (
    RandomGenerator,
    RandomDatetimeGenerator,
    RandomFloatGenerator,
    RandomIntGenerator,
    RandomStrGenerator
)
from daos.base.database.model.model import BaseDBDaoModel


class BaseModelFactory:
    # default generators
    generator_map: Dict[Column | Type, RandomGenerator] = {
        str: RandomStrGenerator(),
        int: RandomIntGenerator(),
        float: RandomFloatGenerator(),
        datetime: RandomDatetimeGenerator()
    }
    
    def __init__(self, model: Type[BaseDBDaoModel], metadata: Metadata = Metadata,):
        self.model = model
        self.metadata = metadata
        self.current_build = {}
    
    def register_generator(self, key: Column | Type, generator_cls: Type[RandomGenerator], **kwargs):
        generator = generator_cls(**kwargs)
        generator.factory = self

        self.generator_map[key] = generator

    def create_many(self, count: int) -> List[BaseDBDaoModel]:
        return [self.create() for _ in range(count)]

    def create(self) -> BaseDBDaoModel:
        for c in self.model.get_columns().values():
            if not c.primary_key:
                key = c if c in self.generator_map else c.type.python_type
                if key not in self.generator_map:
                    raise Exception(f'Generator not registered under key : {key}')
                self.current_build[c.name] = self.generator_map[key].get()
        return self.model(**self.current_build)
