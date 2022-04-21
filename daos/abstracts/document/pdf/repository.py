from abc import ABC
from typing import Type, Generic, TypeVar

from ..repository import BaseDocRepository as Base

T = TypeVar('T')


class PdfDocumentRepository(Base[T], Generic[T], ABC):
    def __init__(self, model: Type[T], path: str):
        super().__init__(model=model, path=path, filetype='.pdf')
