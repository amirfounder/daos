from daos.base.document.html import BaseHtmlDocumentModel


class NewsArticleHtmlDocumentModel(BaseHtmlDocumentModel):
    def __init__(self, path: str):
        super().__init__(path)
