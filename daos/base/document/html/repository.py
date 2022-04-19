from abc import ABC
from typing import Type, TypeVar, Generic

from daos.base.document.base import BaseDocumentRepository as Base
from daos.base.document.utils import FileFormat

T = TypeVar('T')


class BaseHtmlDocumentRepository(Base[T], Generic[T], ABC):
    def __init__(self, model: Type[T], path: str):
        super().__init__(model, path, FileFormat.HTML)
