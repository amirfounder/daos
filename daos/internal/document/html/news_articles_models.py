from daos.abstracts.document.model import BaseDocModel as DocBase
from daos.internal.abstracts.doc_index_model import BaseHtmlDocIndexModel as DbBase

class NewsArticleHtmlDocumentNoJSModel(DocBase): ...

class NewsArticleHtmlDocumentRawModel(DocBase): ...

class NewsArticleHtmlDocumentHtmlOnlyModel(DocBase): ...

class NewsArticleHtmlDocumentIndexModel(DbBase):
    __tablename__ = 'news_article_html_document_index_model'
