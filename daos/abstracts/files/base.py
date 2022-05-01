import os.path
from os import listdir, makedirs
from os.path import isfile, exists
from pathlib import Path
from typing import Any


# noinspection PyPropertyDefinition,PyTypeChecker
class File:
    dir_path: str
    read_mode: str = 'r'
    write_mode: str = 'w'
    suffix: str
    encoding: str = 'utf-8'
    max_file_size: int = 25 * 1000 * 1000

    def __init__(self, contents: Any = '', path: str = None):
        self._create_folders()
        self._contents = contents
        self.path = path or self.next_file_path
        self.pathlib_path = Path(self.path)
        self.filename = self.pathlib_path.name
        self.id = self.pathlib_path.stem

        if not exists(self.path):
            open(self.path, 'x').close()

    @classmethod
    def _create_folders(cls):
        if isfile(cls.dir_path):
            raise Exception(f'Path is a file. Cannot create directory: {cls.dir_path}')
        if not exists(cls.dir_path):
            makedirs(cls.dir_path)

    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, value):
        self._contents = value
    
    @classmethod
    @property
    def next_file_id(cls):
        return cls.files_count + 1

    @classmethod
    @property
    def next_file_path(cls):
        return cls.dir_path + '/' + str(cls.next_file_id) + cls.suffix
    
    @classmethod
    @property
    def last_file_path(cls):
        if cls.files_count == 0:
            open((path := cls.next_file_path), 'x').close()
            return path
        else:
            return cls.dir_path + '/' + str(cls.files_count) + cls.suffix

    @classmethod
    @property
    def files_count(cls) -> int:
        return len(listdir(cls.dir_path))

    @classmethod
    @property
    def files(cls):
        return [cls.dir_path + '/' + name + cls.suffix for name in listdir(cls.dir_path)]

    @property
    def size(self):
        return os.path.getsize(self.path)

    @property
    def exceeds_max_file_size(self):
        return self.size > self.max_file_size

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
            self.path = self.next_file_path

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

        for path in cls.files:
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
