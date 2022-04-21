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

    def build_path_from_id(self, identifier: str | int):
        return self.path + '/' + str(identifier) + self.model.suffix

    def build_next_path(self):
        return self.build_path_from_id(str(len(listdir(self.path)) + 1))

    def create(self, identifier: str | int = None, path: str = None):
        if identifier:
            path = self.build_path_from_id(str(identifier))
        elif path:
            path = path
        else:
            path = self.build_next_path()

        instance = self.model(path=path)
        instance.flush_contents()

        return instance

    def get_all(self):
        instances = []

        for filename in listdir(self.path):
            if isfile((path := self.path + '/' + filename)):
                instance = self.model(path=path)
                instance.load_contents()
                instances.append(instance)

        return instances

    def get(self, identifier: str | int):
        filename = next(iter([f for f in listdir(self.path) if f == str(identifier) + self.model.suffix]), None)

        if filename:
            path = self.path + '/' + filename
            instance = self.model(path=path)
            instance.load_contents()
            return instance

    def save(self, instance):
        if not instance.path:
            instance.set_path(self.build_next_path())

        instance.flush_contents()

        return instance

    def update(self, instance):
        if not instance.path:
            raise Exception('Path not set. Save instead ...')

        instance.flush_contents()

        return instance

    def delete(self, identifier: str | int):
        instance = self.get(str(identifier))
        if instance:
            os.remove(instance.path)
