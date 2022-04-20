from daos.abstracts.document.html.repository import BaseHtmlDocRepository as DocBase
from daos.abstracts.database.repository import BaseDBRepository as DBBase
from daos.internal.paths import Paths


class NewsArticleHtmlDocumentNoJSRepository(DocBase):
    def __init__(self):
        super().__init__(Paths.NEWS_ARTICLE_NO_JS_DIR_PATH.value)

class NewsArticleHtmlDocumentRawRepository(DocBase):
    def __init__(self):
        super().__init__(Paths.NEWS_ARTICLE_RAW_DIR_PATH.value)

class NewsArticleHtmlDocumentHtmlOnlyRepository(DocBase):
    def __init__(self):
        super().__init__(Paths.NEWS_ARTICLE_HTML_ONLY_DIR_PATH.value)

class NewsArticleHtmlDocumentIndexRepository(DBBase): ...
