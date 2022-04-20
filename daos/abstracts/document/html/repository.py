from abc import ABC
from typing import Type

from ..repository import BaseDocRepository


class BaseHtmlDocumentRepository(BaseDocRepository, ABC):
    def __init__(self, model: Type, path: str):
        super().__init__(model, path, '.html')
