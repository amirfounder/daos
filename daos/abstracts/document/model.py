from typing import Any, Optional
from pathlib import Path

from ..model import BaseModel


class DocumentModel(BaseModel):
    def __init__(
            self,
            path: Optional[str] = None,
            read_mode: str = 'r',
            write_mode: str = 'w'
    ):
        self.read_mode = read_mode
        self.write_mode = write_mode
        self.contents: Optional[str] = ''
        self.set_path(path or '')

    # noinspection PyAttributeOutsideInit
    def set_path(self, path: str):
        self.path = path
        self.pathlib_path = Path(path)
        self.filename = self.pathlib_path.name
        self.id = self.pathlib_path.stem
        self.filetype = self.pathlib_path.suffix

    def load_contents(self, contents: Any):
        self.contents = str(contents)

    def load_contents_from_system(self):
        with open(self.path, self.read_mode) as f:
            self.contents = f.read()
