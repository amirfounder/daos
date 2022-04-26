from os import listdir
from os.path import isfile
from pathlib import Path
from typing import Any


class File:
    path: str
    read_mode: str = 'r'
    write_mode: str = 'w'
    suffix: str
    encoding: str = 'utf-8'

    def __init__(self, contents: Any = '', path: str = None):
        self.contents = contents
        self.path = path or self._next_document_path()
        self.pathlib_path = Path(self.path)
        self.filename = self.pathlib_path.name
        self.id = self.pathlib_path.stem

    def _next_document_id(self):
        return len(listdir(self.path)) + 1

    def _next_document_path(self):
        return self.path + '/' + str(self._next_document_id()) + self.suffix

    def load(self):
        if not self.id:
            raise Exception('No id specified.')

        kwargs = {
            'file': self.path,
            'mode': self.read_mode
        }

        if self.read_mode != 'rb':
            kwargs['encoding'] = self.encoding

        with open(**kwargs) as f:
            self.contents = f.read()

        return self.contents

    def flush(self):
        kwargs = {
            'file': self.path,
            'mode': self.write_mode
        }

        if self.write_mode != 'wb':
            kwargs['encoding'] = self.encoding

        with open(**kwargs) as f:
            f.write(self.contents)

    @classmethod
    def all(cls, load_contents: bool = True):
        for filename in listdir(cls.path):
            if isfile((path := cls.path + '/' + filename)):
                instance = cls(path=path)
                if load_contents:
                    instance.load()
                yield instance
