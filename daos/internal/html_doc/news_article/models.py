from daos.base.document.html.model import BaseHtmlDocumentModel as DocumentBase
from daos.base.database.model import BaseDatabaseModel as DatabaseBase


class NewsArticleHtmlDocumentNoJSModel(DocumentBase):
    ...


class NewsArticleHtmlDocumentRawModel(DocumentBase):
    ...


class NewsArticleHtmlDocumentHtmlOnlyModel(DocumentBase):
    ...


class NewsArticleHtmlDocumentIndexModel(DatabaseBase):
    __tablename__ = 'news_article_html_document_index'
