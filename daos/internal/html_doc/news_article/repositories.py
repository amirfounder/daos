from daos.base.document.html.repository import BaseHtmlDocumentRepository as Base
from daos.base.database import BaseDatabaseRepository
from daos.internal.paths import Paths

from .models import (
    NewsArticleHtmlDocumentNoJSModel as NoJsModel,
    NewsArticleHtmlDocumentHtmlOnlyModel as HtmlOnlyModel,
    NewsArticleHtmlDocumentRawModel as RawModel,
    NewsArticleHtmlDocumentIndexModel as IndexModel
)


class NewsArticleHtmlDocumentNoJsRepository(Base[NoJsModel]):
    def __init__(self):
        super().__init__(
            model=NoJsModel,
            path=Paths.NEWS_ARTICLE_NO_JS_DIR_PATH.value
        )


class NewsArticleHtmlDocumentHtmlOnlyRepository(Base[HtmlOnlyModel]):
    def __init__(self):
        super().__init__(
            model=HtmlOnlyModel,
            path=Paths.NEWS_ARTICLE_HTML_ONLY_DIR_PATH.value
        )


class NewsArticleHtmlDocumentRawRepository(Base[RawModel]):
    def __init__(self):
        super().__init__(
            model=RawModel,
            path=Paths.NEWS_ARTICLE_RAW_DIR_PATH.value
        )


class NewsArticleHtmlDocumentIndexRepository(BaseDatabaseRepository[IndexModel]):
    def __init__(self):
        super().__init__(IndexModel)
