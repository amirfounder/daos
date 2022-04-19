from daos.base.document.html.repository import BaseHtmlDocumentRepository as Base
from daos.internal.paths import Paths

from .models import (
    NewsArticleHtmlDocumentNoJSModel,
    NewsArticleHtmlDocumentHtmlOnlyModel,
    NewsArticleHtmlDocumentRawModel
)


class NewsArticleHtmlDocumentNoJsRepository(Base[NewsArticleHtmlDocumentNoJSModel]):
    def __init__(self):
        super().__init__(
            model=NewsArticleHtmlDocumentNoJSModel,
            path=Paths.NEWS_ARTICLE_NO_JS_DIR_PATH.value
        )


class NewsArticleHtmlDocumentHtmlOnlyRepository(Base[NewsArticleHtmlDocumentHtmlOnlyModel]):
    def __init__(self):
        super().__init__(
            model=NewsArticleHtmlDocumentHtmlOnlyModel,
            path=Paths.NEWS_ARTICLE_HTML_ONLY_DIR_PATH.value
        )


class NewsArticleHtmlDocumentRawRepository(Base[NewsArticleHtmlDocumentRawModel]):
    def __init__(self):
        super().__init__(
            model=NewsArticleHtmlDocumentRawModel,
            path=Paths.NEWS_ARTICLE_RAW_DIR_PATH.value
        )
