import os
from abc import ABC
from os import listdir
from os.path import isfile
from typing import TypeVar, Optional, Generic, Type

from ..repository import BaseRepository

T = TypeVar('T')


class BaseDocRepository(BaseRepository[T], Generic[T], ABC):
    def __init__(self, model: Type[T], path: Optional[str],):
        super().__init__(model)

        if not os.path.exists(path):
            os.makedirs(path)

        self.path = path

    def build_path_from_id(self, identifier):
        return self.path + '/' + identifier + self.model.suffix

    def build_next_path(self):
        return self.build_path_from_id(str(len(listdir(self.path)) + 1))

    def create(self, identifier: str = None, path: str = None):
        if identifier:
            path = self.build_path_from_id(identifier)
        elif path:
            path = path
        else:
            path = self.build_next_path()

        instance = self.model(path=path)
        return self.save(instance)

    def get_all(self):
        return [
            self.model(path=path) for
            filename in listdir(self.path) if
            isfile((path := f'{self.path}/{filename}'))
        ]

    def get(self, identifier: str):
        filename = next(iter([f for f in listdir(self.path) if f == identifier + self.model.suffix]), None)
        return self.model(path=self.path + '/' + filename)

    def save(self, instance):
        if not instance.path:
            instance.set_path(self.build_next_path())

        with open(instance.path, mode=self.model.write_mode, encoding=self.model.encoding) as f:
            f.write(instance.contents)

        return instance

    def update(self, instance):
        if not instance.path:
            raise Exception('Path not set. Save instead ...')

        with open(instance.path, mode=self.model.write_mode, encoding=self.model.encoding) as f:
            f.write(instance.contents)

        return instance

    def delete(self, identifier):
        instance = self.get(identifier)
        if instance:
            os.remove(instance.path)
