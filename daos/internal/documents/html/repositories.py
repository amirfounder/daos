from daos.abstracts.document.html.repository import BaseHtmlDocRepository as DocRepository
from daos.abstracts.document.html.model import HtmlDocumentModel as DocModel
from daos.abstracts.database.repository import BaseDBRepository as DBRepository
from daos.internal.base.doc_index_model import HtmlDocumentIndexItem
from daos.internal.paths import Paths


class GoogleSearchResultsHtmlDocumentNoJSRepository(DocRepository[DocModel]):
    def __init__(self):
        super().__init__(DocModel, Paths.GOOGLE_SEARCH_RESULTS_NO_JS_DIR_PATH.value)

class GoogleSearchResultsHtmlDocumentRawRepository(DocRepository[DocModel]):
    def __init__(self):
        super().__init__(DocModel, Paths.GOOGLE_SEARCH_RESULTS_RAW_DIR_PATH.value)

class GoogleSearchResultsHtmlDocumentHtmlOnlyRepository(DocRepository[DocModel]):
    def __init__(self):
        super().__init__(DocModel, Paths.GOOGLE_SEARCH_RESULTS_HTML_ONLY_DIR_PATH.value)

class GoogleSearchResultsHtmlDocumentIndexRepository(DBRepository[HtmlDocumentIndexItem]):
    def __init__(self):
        super().__init__(HtmlDocumentIndexItem)

class NewsArticleHtmlDocumentNoJSRepository(DocRepository[DocModel]):
    def __init__(self):
        super().__init__(DocModel, Paths.NEWS_ARTICLE_NO_JS_DIR_PATH.value)

class NewsArticleHtmlDocumentRawRepository(DocRepository[DocModel]):
    def __init__(self):
        super().__init__(DocModel, Paths.NEWS_ARTICLE_RAW_DIR_PATH.value)

class NewsArticleHtmlDocumentHtmlOnlyRepository(DocRepository[DocModel]):
    def __init__(self):
        super().__init__(DocModel, Paths.NEWS_ARTICLE_HTML_ONLY_DIR_PATH.value)

class NewsArticleHtmlDocumentIndexRepository(DBRepository[HtmlDocumentIndexItem]):
    def __init__(self):
        super().__init__(HtmlDocumentIndexItem)
