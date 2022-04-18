from daos.base import BaseDatabaseDao
from daos.internal import NewsArticleHtmlDocumentIndexModel


class NewsArticleHtmlDocumentIndexDao(BaseDatabaseDao):
    def __init__(self):
        super().__init__('connection_string', NewsArticleHtmlDocumentIndexModel)
