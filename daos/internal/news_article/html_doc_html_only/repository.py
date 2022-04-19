from daos.base.document.html.repository import BaseHtmlDocumentRepository as Base
from daos.internal.paths import Paths

from .model import NewsArticleHtmlDocumentHtmlOnlyModel as Model

PATH = Paths.NEWS_ARTICLE_HTML_ONLY_DIR_PATH.value


class NewsArticleHtmlDocumentHtmlOnlyRepository(Base):
    def __init__(self):
        super().__init__(Model, PATH)
