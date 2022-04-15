from random import random
from typing import TypeVar, Generic

from pgsql_repository.core import Metadata

T = TypeVar('T')


class Factory(Generic[T]):
    def __init__(self, model: T, metadata: Metadata = Metadata):
        self.model = model
        self.metadata = metadata

    def _model_to_types_dict(self):
        pass

    def _model_from_dict(self):
        pass
