from daos.base.document.html.repository import BaseHtmlDocumentRepository as Base
from daos.internal.paths import Paths

from .model import NewsArticleHtmlDocumentRawModel as Model

PATH = Paths.NEWS_ARTICLE_RAW_DIR_PATH.value


class NewsArticleHtmlDocumentRawRepository(Base):
    def __init__(self):
        super().__init__(Model, PATH)
