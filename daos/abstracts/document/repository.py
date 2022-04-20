import os
from abc import ABC
from os import listdir
from os.path import isfile
from typing import TypeVar, Optional, Generic, Type

from ..repository import BaseRepository

T = TypeVar('T')


class BaseDocRepository(BaseRepository[T], Generic[T], ABC):
    def __init__(
            self,
            model: Type[T],
            path: Optional[str],
            filetype: str,
            write_mode: str = 'w',
            read_mode: str = 'r',
            encoding: str = 'utf-8'
    ):
        super().__init__(model)

        if not os.path.exists(path):
            os.makedirs(path)

        if not filetype.startswith('.'):
            filetype = '.' + filetype

        self.path = path
        self.filetype = filetype
        self.write_mode = write_mode
        self.read_mode = read_mode
        self.encoding = encoding

    def _path(self, identifier):
        return self.path + '/' + identifier + self.filetype

    def _next_path(self):
        return self._path(str(len(listdir(self.path)) + 1))

    def create(self, **kwargs):
        instance = self.model(**kwargs)

        if _id := kwargs.get('id'):
            path = self._path(_id)
        elif path := kwargs.get('path'):
            path = path
        else:
            path = self._next_path()

        instance.set_path(path)

        return self.save(instance)

    def get_all(self):
        return [
            self.model(path=path, encoding=self.encoding) for
            file in listdir(self.path) if
            isfile((path := f'{self.path}/{file}'))
        ]

    def get(self, identifier):
        return next(iter([i for i in self.get_all() if i.id == str(identifier)]), None)

    def save(self, instance):
        if not instance.path:
            instance.set_path(self._next_path())

        with open(instance.path, mode=self.write_mode, encoding=self.encoding) as f:
            f.write(instance.contents)

        return instance

    def update(self, instance):
        if not instance.path:
            raise Exception('Path not set. Save instead ...')

        with open(instance.path, mode=self.write_mode, encoding=self.encoding) as f:
            f.write(instance.contents)

        return instance

    def delete(self, identifier):
        instance = self.get(identifier)
        if instance:
            os.remove(instance.path)
