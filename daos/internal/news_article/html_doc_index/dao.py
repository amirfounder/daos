from daos.base import BaseDatabaseDao
from daos.internal.news_article.html_doc_index.model import NewsArticleHtmlDocumentIndexModel


class NewsArticleHtmlDocumentIndexDao(BaseDatabaseDao):
    def __init__(self):
        super().__init__('postgresql://postgres:root@localhost:5432/postgres', NewsArticleHtmlDocumentIndexModel)
