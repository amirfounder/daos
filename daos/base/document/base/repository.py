import os
from abc import ABC
from os import listdir
from os.path import isfile
from pathlib import Path
from typing import List, Type, TypeVar, Generic
from ntpath import basename

from daos.base.base.repository import BaseRepository
from daos.base.document.utils import FileFormat

T = TypeVar('T')


class BaseDocumentRepository(BaseRepository, Generic[T], ABC):
    """
    TODO: Create a memory cache of file object ids to make sure we don't accidentally mis-create document objects.
    """
    def __init__(self, model: Type[T], path: str, file_format: FileFormat):
        super().__init__(model)
        self.path = path
        self.file_format = file_format

        if not os.path.exists(path):
            os.makedirs(path)

        if not os.path.isdir(path):
            raise Exception(f'Path is not a directory : {path}')

    def _list_file_paths(self) -> List[Path]:
        return [Path(path) for f in listdir(self.path) if isfile(path := f'{self.path}/{f}')]

    def _next_document_id(self) -> int:
        return len(self._list_file_paths()) + 1

    def _next_document_path(self) -> str:
        return f'{self.path}/{self._next_document_id()}{self.file_format.value}'

    def get_all(self) -> List[T]:
        models = []

        for path in self._list_file_paths():
            model = self.model()
            model.set_path(path)
            model.load_contents()

        return models

    def get_by_id(self, _id: int | str) -> T | None:
        path = next(iter([path for path in self._list_file_paths() if path.stem == _id]))

        if not path:
            return

        instance = self.model()
        instance.set_path(path)
        instance.load_contents()

        return instance

    def get_by_path(self, path: str | Path) -> T | None:
        if not isinstance(path, Path):
            path = Path(path)
        return self.get_by_id(path.stem)

    def save(self, instance: T) -> T:
        if instance.get_path():
            raise Exception(f'Instance already has path. Update instead.')

        instance.set_path(self._next_document_path())

        with open(instance.get_path(), 'w', encoding='utf-8') as file:
            file.write(instance.contents)

        return instance

    # noinspection PyMethodMayBeStatic
    def update(self, instance: T) -> T:
        with open(instance.get_path(), 'w', encoding='utf-8') as file:
            file.write(instance.contents)

        return instance

    def delete(self, _id: int | str) -> None:
        instance = self.get_by_id(_id)

        if instance:
            os.remove(instance.get_path())
