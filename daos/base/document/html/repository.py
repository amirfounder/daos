from abc import ABC
from typing import Type

from daos.base.document.base import BaseDocumentRepository
from daos.base.document.utils import FileFormat


class BaseHtmlDocumentRepository(BaseDocumentRepository, ABC):
    def __init__(self, model: Type, path: str):
        super().__init__(model, path, FileFormat.HTML)
