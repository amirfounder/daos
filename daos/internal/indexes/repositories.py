from daos.abstracts.database.repository import BaseDBRepository as DBRepository
from daos.internal.base.doc_index_model import HtmlDocumentIndexItem


class NewsArticleHtmlDocumentIndexRepository(DBRepository[HtmlDocumentIndexItem]):
    def __init__(self): super().__init__(HtmlDocumentIndexItem)


class GoogleSearchResultsHtmlDocumentIndexRepository(DBRepository[HtmlDocumentIndexItem]):
    def __init__(self): super().__init__(HtmlDocumentIndexItem)
