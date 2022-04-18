from abc import ABC
from typing import Any

from daos.base.base.model import BaseModel


class BaseDocumentModel(BaseModel, ABC):
    def __init__(self, contents: Any = None, path: str = None):
        self.contents = contents
        self.path = path

    def read(self, mode: str = 'r') -> str:
        with open(self.path, mode) as f:
            return f.read()

    def load_contents(self):
        self.contents = self.read()
