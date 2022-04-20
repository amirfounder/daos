from abc import ABC
from typing import Any, Optional
from pathlib import Path

from ..model import BaseModel


class BaseDocModel(BaseModel, ABC):
    def __init__(
            self,
            path: Optional[str] = None,
            filetype: Optional[str] = None,
            read_mode: str = 'r',
            write_mode: str = 'w'
    ):
        self.path = path
        self.filetype = filetype
        self.read_mode = read_mode
        self.write_mode = write_mode
        self.pathlib_path = Path(path)
        self.filename = self.pathlib_path.name
        self.id = self.pathlib_path.stem
        self.contents: Optional[str] = None

    def load_contents(self, contents: Any):
        self.contents = str(contents)

    def load_contents_from_system(self):
        with open(self.path, self.read_mode) as f:
            self.contents = f.read()
