from abc import ABC
from typing import Any, Optional

from pathlib import Path

from daos.base.base.model import BaseModel


class BaseDocumentModel(BaseModel, ABC):
    def __init__(self, contents: Optional[Any] = None):
        self._contents = str(contents)
        self._path: Optional[Path] = None
        self._id: Optional[int] = None

    def get_id(self):
        return self._id

    def get_path(self):
        return self._path

    def set_path(self, path: str):
        if not self._path:
            self._path = Path(path)
            if self._path.stem.isdigit():
                self._id = self._path.stem
            else:
                raise Exception(f'Path stem is not digit : {self._path}')
        else:
            raise Exception(f'Cannot set path. Path already set : {self._path}')

    def get_contents(self):
        return self._contents

    def set_contents(self, contents: Any):
        self._contents = str(contents)

    def read(self, mode: str = 'r') -> str:
        with open(self._path, mode) as f:
            self.contents = f.read()
            return self.contents
