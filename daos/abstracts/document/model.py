from typing import Any, Optional
from pathlib import Path

from ..model import BaseModel


class DocumentModel(BaseModel):
    def __init__(
            self,
            path: Optional[str] = None,
            read_mode: str = 'r',
            write_mode: str = 'w',
            encoding: str = 'utf-8'
    ):
        self.set_path(path or '')
        self.read_mode = read_mode
        self.write_mode = write_mode
        self.encoding = encoding
        self.contents: Optional[str] = ''

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
