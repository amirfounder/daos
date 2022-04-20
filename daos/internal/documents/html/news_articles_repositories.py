from daos.abstracts.document.html.repository import BaseHtmlDocRepository as DocBase
from daos.abstracts.database.repository import BaseDBRepository as DBBase
from daos.internal.paths import Paths


from .news_articles_models import (
    NewsArticleHtmlDocumentIndexModel as Index,
    NewsArticleHtmlDocumentRawModel as Raw,
    NewsArticleHtmlDocumentHtmlOnlyModel as HtmlOnly,
    NewsArticleHtmlDocumentNoJSModel as NoJs
)


class NewsArticleHtmlDocumentNoJSRepository(DocBase):
    def __init__(self):
        super().__init__(NoJs, Paths.NEWS_ARTICLE_NO_JS_DIR_PATH.value)

class NewsArticleHtmlDocumentRawRepository(DocBase):
    def __init__(self):
        super().__init__(Raw, Paths.NEWS_ARTICLE_RAW_DIR_PATH.value)

class NewsArticleHtmlDocumentHtmlOnlyRepository(DocBase):
    def __init__(self):
        super().__init__(HtmlOnly, Paths.NEWS_ARTICLE_HTML_ONLY_DIR_PATH.value)

class NewsArticleHtmlDocumentIndexRepository(DBBase):
    def __init__(self):
        super().__init__(Index)
