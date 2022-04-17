from daos.base.abstract.dao import BaseDao
from daos.base.document.abstract.model import BaseDocumentModel


class BaseDocumentDao(BaseDao):
    def get_all(self):
        pass

    def get_by_id(self, _id: int | str):
        pass

    def create(self, entity: BaseDocumentModel):
        pass

    def update(self, entity: BaseDocumentModel):
        pass

    def delete(self, _id: int | str):
        pass
