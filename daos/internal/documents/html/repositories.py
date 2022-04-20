from daos.abstracts.document.html.repository import BaseHtmlDocRepository as DocBase
from daos.abstracts.document.html.model import HtmlDocumentModel
from daos.abstracts.database.repository import BaseDBRepository as DBBase
from daos.internal.base.doc_index_model import HtmlDocumentIndexItem
from daos.internal.paths import Paths


class GoogleSearchResultsHtmlDocumentNoJSRepository(DocBase):
    def __init__(self):
        super().__init__(HtmlDocumentModel, Paths.GOOGLE_SEARCH_RESULTS_NO_JS_DIR_PATH.value)

class GoogleSearchResultsHtmlDocumentRawRepository(DocBase):
    def __init__(self):
        super().__init__(HtmlDocumentModel, Paths.GOOGLE_SEARCH_RESULTS_RAW_DIR_PATH.value)

class GoogleSearchResultsHtmlDocumentHtmlOnlyRepository(DocBase):
    def __init__(self):
        super().__init__(HtmlDocumentModel, Paths.GOOGLE_SEARCH_RESULTS_HTML_ONLY_DIR_PATH.value)

class GoogleSearchResultsHtmlDocumentIndexRepository(DBBase):
    def __init__(self):
        super().__init__(HtmlDocumentIndexItem)

class NewsArticleHtmlDocumentNoJSRepository(DocBase):
    def __init__(self):
        super().__init__(HtmlDocumentModel, Paths.NEWS_ARTICLE_NO_JS_DIR_PATH.value)

class NewsArticleHtmlDocumentRawRepository(DocBase):
    def __init__(self):
        super().__init__(HtmlDocumentModel, Paths.NEWS_ARTICLE_RAW_DIR_PATH.value)

class NewsArticleHtmlDocumentHtmlOnlyRepository(DocBase):
    def __init__(self):
        super().__init__(HtmlDocumentModel, Paths.NEWS_ARTICLE_HTML_ONLY_DIR_PATH.value)

class NewsArticleHtmlDocumentIndexRepository(DBBase):
    def __init__(self):
        super().__init__(HtmlDocumentIndexItem)
