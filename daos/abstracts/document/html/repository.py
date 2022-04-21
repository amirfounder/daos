from abc import ABC
from typing import TypeVar, Generic, Type

from ..repository import BaseDocRepository

T = TypeVar('T')


class BaseHtmlDocRepository(BaseDocRepository[T], Generic[T], ABC):
    def __init__(self, model: Type[T], path: str):
        super().__init__(model=model, path=path, filetype='.html')
