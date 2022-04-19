from daos.base.document.html.model import BaseHtmlDocumentModel as DocumentBase
from daos.internal.html_doc.base.models import BaseHtmlDocumentIndexModel as DatabaseBase


class NewsArticleHtmlDocumentNoJSModel(DocumentBase):
    ...


class NewsArticleHtmlDocumentRawModel(DocumentBase):
    ...


class NewsArticleHtmlDocumentHtmlOnlyModel(DocumentBase):
    ...


class NewsArticleHtmlDocumentIndexModel(DatabaseBase):
    __tablename__ = 'news_article_html_document_indices'
