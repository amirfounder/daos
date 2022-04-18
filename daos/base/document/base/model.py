from abc import ABC
from typing import Any, Optional

from ntpath import basename

from daos.base.base.model import BaseModel


class BaseDocumentModel(BaseModel, ABC):
    def __init__(self, contents: Optional[Any] = None, path: Optional[str] = None):
        self.contents = contents
        self._path = path
        self._id = basename(path)

    def get_id(self):
        return self._id

    def get_path(self):
        return self._path

    def set_path(self, path: str):
        if not self._path:
            self._path = path
            self._id = basename(path)

        raise Exception(f'Cannot set path. Path already set : {self._path}')

    def read(self, mode: str = 'r') -> str:
        with open(self._path, mode) as f:
            self.contents = f.read()
            return self.contents
