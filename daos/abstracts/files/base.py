import os.path
from os import listdir, makedirs
from os.path import isfile, exists
from pathlib import Path
from typing import Any


class File:
    dir_path: str
    read_mode: str = 'r'
    write_mode: str = 'w'
    suffix: str
    encoding: str = 'utf-8'

    def __init__(self, contents: Any = '', path: str = None):
        self.create_folders()
        self.contents = contents
        self.path = path or self.next_document_path()
        self.pathlib_path = Path(self.path)
        self.filename = self.pathlib_path.name
        self.id = self.pathlib_path.stem
        self.flush()

    @classmethod
    def create_folders(cls):
        if isfile(cls.dir_path):
            raise Exception(f'Path is a file. Cannot create directory: {cls.dir_path}')
        if not exists(cls.dir_path):
            makedirs(cls.dir_path)

    @classmethod
    def list_file_paths(cls):
        return [cls.dir_path + '/' + name + cls.suffix for name in listdir(cls.dir_path)]

    @classmethod
    def next_document_id(cls):
        return len(listdir(cls.dir_path)) + 1

    @classmethod
    def next_document_path(cls):
        return cls.dir_path + '/' + str(cls.next_document_id()) + cls.suffix

    @classmethod
    def last_document_path(cls):
        return cls.dir_path + '/' + str(len(listdir(cls.dir_path))) + cls.suffix

    def get_size(self):
        return os.path.getsize(self.path)

    def set_contents(self, contents: Any):
        self.contents = contents

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
            self.path = self.next_document_path()

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
        cls.create_folders()

        for path in cls.list_file_paths():
            if isfile(path):
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
