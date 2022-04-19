from daos.base.document.html.dao import BaseHtmlDocumentDao as Base
from daos.internal.paths import Paths
from .model import NewsArticleHtmlDocumentRawModel as Model

PATH = Paths.NEWS_ARTICLE_RAW_DIR_PATH.value


class NewsArticleHtmlDocumentRawDao(Base):
    def __init__(self):
        super().__init__(Model, PATH)
