from os import listdir, makedirs
from os.path import isfile, exists
from pathlib import Path
from typing import Any


class File:
    path: str
    read_mode: str = 'r'
    write_mode: str = 'w'
    suffix: str
    encoding: str = 'utf-8'

    def __init__(self, contents: Any = '', path: str = None):
        self._create_folders()
        self.contents = contents
        self.path = path or self._next_document_path()
        self.pathlib_path = Path(self.path)
        self.filename = self.pathlib_path.name
        self.id = self.pathlib_path.stem

    @classmethod
    def _create_folders(cls):
        if isfile(cls.path):
            raise Exception(f'Path is a file. Cannot create directory: {cls.path}')
        if not exists(cls.path):
            makedirs(cls.path)

    def _next_document_id(self):
        return len(listdir(self.path)) + 1

    def _next_document_path(self):
        return self.path + '/' + str(self._next_document_id()) + self.suffix

    def load(self):
        if not self.path:
            raise Exception('No path specified.')

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
        if not self.path:
            self.path = self._next_document_path()

        kwargs = {
            'file': self.path,
            'mode': self.write_mode
        }

        if self.write_mode != 'wb':
            kwargs['encoding'] = self.encoding

        with open(**kwargs) as f:
            f.write(self.contents)

    @classmethod
    def all(cls, load: bool = False, **kwargs):
        cls._create_folders()

        for filename in listdir(cls.path):
            if isfile((path := cls.path + '/' + filename)):
                instance = cls(path=path)

                if kwargs:

                    failed_filter = False
                    for k, v in kwargs.items():
                        if hasattr(instance, k) and getattr(instance, k, None) != v:
                            failed_filter = True
                            break

                    if failed_filter:
                        continue

                if load:
                    instance.load()

                yield instance
