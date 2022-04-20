from daos.abstracts.document.html.model import BaseHtmlDocModel as DocBase
from daos.internal.abstracts.doc_index_model import BaseHtmlDocIndexModel as DbBase


class NewsArticleHtmlDocumentNoJSModel(DocBase):
    ...

class NewsArticleHtmlDocumentRawModel(DocBase):
    ...

class NewsArticleHtmlDocumentHtmlOnlyModel(DocBase):
    ...

class NewsArticleHtmlDocumentIndexModel(DbBase):
    ...
