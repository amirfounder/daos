import os
from abc import ABC
from os import listdir
from os.path import isfile
from typing import List, Type
from ntpath import basename

from daos.base.base.dao import BaseDao
from daos.base.document.base.model import BaseDocumentModel
from daos.base.document.utils import FileFormat


class BaseDocumentDao(BaseDao, ABC):
    def __init__(self, model: Type, path: str, file_format: FileFormat):
        super().__init__(model)
        self.path = path
        self.file_format = file_format
        if not os.path.exists(path):
            os.makedirs(path)
        if not os.path.isdir(path):
            raise Exception(f'Path is not a directory : {path}')

    def _list_file_paths(self):
        return [path for path in listdir(self.path) if isfile(path)]

    def _next_document_id(self) -> int:
        return len(self._list_file_paths()) + 1

    def _next_document_path(self) -> str:
        return f'{self.path}/{self._next_document_id()}{self.file_format.value}'

    def get_all(self) -> List[BaseDocumentModel]:
        models = [self.model(path=path) for path in self._list_file_paths()]
        for model in models:
            model.load_contents()
        return models

    def get_by_id(self, _id: int | str) -> BaseDocumentModel | None:
        path = next(iter([path for path in self._list_file_paths() if basename(path) == _id]))
        if not path:
            return
        instance = self.model(path=path)
        instance.load_contents()
        return instance

    def save(self, instance: BaseDocumentModel) -> BaseDocumentModel:
        if not instance.path:
            instance.path = self._next_document_path()
        if not instance.path.startswith(self.path):
            raise Exception(f'Cannot create model outside dao path : Expected : {self.path}... Got : {instance.path}')
        with open(instance.path, 'w') as file:
            file.write(instance.contents)
        return instance

    def update(self, instance: BaseDocumentModel) -> BaseDocumentModel:
        with open(instance.path, 'w') as file:
            file.write(instance.contents)
        return instance

    def delete(self, _id: int | str) -> None:
        instance = self.get_by_id(_id)
        if instance:
            os.remove(instance.path)
