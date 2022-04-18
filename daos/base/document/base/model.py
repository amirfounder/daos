import os
from abc import ABC
from typing import Any

from daos.base.base.model import BaseModel


class BaseDocumentModel(BaseModel, ABC):
    def __init__(self, path: str, contents: Any = None):
        self.path = path
        self.contents = contents

    def read(self, mode: str = 'r') -> str:
        with open(self.path, mode) as f:
            self.contents = f.read()
        return self.contents

    def write(self, mode: str = 'w') -> None:
        with open(self.path, mode) as f:
            f.write(self.contents)

    def delete(self):
        os.remove(self.path)
