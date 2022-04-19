from daos.base import BaseDatabaseRepository
from daos.internal.news_article.html_doc_index.model import NewsArticleHtmlDocumentIndexModel


class NewsArticleHtmlDocumentIndexRepository(BaseDatabaseRepository):
    def __init__(self):
        super().__init__('postgresql://postgres:root@localhost:5432/postgres', NewsArticleHtmlDocumentIndexModel)
