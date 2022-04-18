from abc import ABC
from os import listdir
from os.path import isfile
from typing import List, Type, Any
from ntpath import basename

from daos.base.base.dao import BaseDao
from daos.base.document.base.model import BaseDocumentModel
from daos.base.document.utils import FileFormat


class BaseDocumentDao(BaseDao, ABC):
    def __init__(self, model: Type, path: str, file_format: FileFormat):
        super().__init__(model)
        self.path = path
        self.file_format = file_format

    def _list_file_paths(self):
        return [p for p in listdir(self.path) if isfile(p)]

    def _next_document_id(self) -> int:
        return len(self._list_file_paths()) + 1

    def _next_document_path(self) -> str:
        return f'{self._next_document_id()}{self.file_format.value}'

    def get_all(self) -> List[BaseDocumentModel]:
        return [self.model(f) for f in self._list_file_paths()]

    def get_by_id(self, _id: int | str) -> BaseDocumentModel | None:
        p = next(iter([p for p in self._list_file_paths() if basename(p) == _id]))
        return self.model(p) if p else None

    def create(self, contents: Any) -> BaseDocumentModel:
        entity = self.model(f'{self.path}/{self._next_document_path()}', contents)
        entity.write()
        return entity

    def update(self, entity: BaseDocumentModel) -> BaseDocumentModel:
        entity.write()
        return entity

    def delete(self, _id: int | str) -> None:
        entity = self.get_by_id(_id)
        if entity:
            entity.delete()
