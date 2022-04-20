from abc import ABC
from typing import TypeVar, Generic

from ..repository import BaseDocRepository

T = TypeVar('T')


class BaseHtmlDocRepository(BaseDocRepository[T], Generic[T], ABC):
    def __init__(self, path: str):
        super().__init__(path, '.html')
