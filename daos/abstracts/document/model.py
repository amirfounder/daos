from typing import Any, Optional
from pathlib import Path

from ..model import BaseModel


class DocumentModel(BaseModel):
    suffix = '.txt'
    read_mode = 'r'
    write_mode = 'w'
    encoding = 'uf-8'

    def __init__(self, path: Optional[str] = None, contents: Optional[str] = None):
        self.set_path(path or '')
        self.contents: Optional[str] = contents or ''

    def set_id(self, identifier: str):
        self.set_path(identifier + self.suffix)

    # noinspection PyAttributeOutsideInit
    def set_path(self, path: str):
        self.path = path
        self.pathlib_path = Path(path)
        self.filename = self.pathlib_path.name
        self.id = self.pathlib_path.stem
        self.suffix = self.pathlib_path.suffix

    def flush_contents(self):
        with open(self.path, self.write_mode, encoding=self.encoding) as f:
            f.write(self.contents)

    def load_contents(self):
        with open(self.path, self.read_mode, encoding=self.encoding) as f:
            self.contents = f.read()
