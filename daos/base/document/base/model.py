from abc import ABC
from typing import Any, Optional

from ntpath import basename

from daos.base.base.model import BaseModel


class BaseDocumentModel(BaseModel, ABC):
    def __init__(self, contents: Optional[Any] = None, path: Optional[str] = None):
        self.contents = contents
        self.path = path
        self.id = basename(path)

    def set_path(self, path: str):
        self.path = path
        self.id = basename(path)

    def read(self, mode: str = 'r') -> str:
        with open(self.path, mode) as f:
            self.contents = f.read()
            return self.contents
