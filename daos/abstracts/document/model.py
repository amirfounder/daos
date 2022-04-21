from typing import Any, Optional
from pathlib import Path

from ..model import BaseModel


class DocumentModel(BaseModel):
    filetype = '.txt'
    read_mode = 'r'
    write_mode = 'w'
    encoding = 'uf-8'

    def __init__(self, path: Optional[str] = None, contents: Optional[str] = None):
        self.set_path(path or '')
        self.contents: Optional[str] = contents or ''

    # noinspection PyAttributeOutsideInit
    def set_path(self, path: str):
        self.path = path
        self.pathlib_path = Path(path)
        self.filename = self.pathlib_path.name
        self.id = self.pathlib_path.stem
        self.filetype = self.pathlib_path.suffix

    def set_contents(self, contents: Any):
        self.contents = str(contents)

    def load_contents(self):
        with open(self.path, self.read_mode, encoding=self.encoding) as f:
            self.contents = f.read()
