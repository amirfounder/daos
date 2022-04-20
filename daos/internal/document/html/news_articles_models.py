from daos.abstracts.document.model import BaseDocModel as DocBase
from daos.internal.abstracts.doc_index_model import BaseHtmlDocIndexModel

class NewsArticleHtmlDocumentNoJSModel(DocBase): ...

class NewsArticleHtmlDocumentRawModel(DocBase): ...

class NewsArticleHtmlDocumentHtmlOnlyModel(DocBase): ...

class NewsArticleHtmlDocumentIndexModel(BaseHtmlDocIndexModel): ...