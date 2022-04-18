from daos.base.document.abstract import BaseDocumentDao
from daos.base.document.html import BaseHtmlDocumentModel
from daos.base.document.utils import FileFormat


class BaseHtmlDocumentDao(BaseDocumentDao):
    def __init__(self, path: str):
        super().__init__(BaseHtmlDocumentModel, path, FileFormat.HTML)
