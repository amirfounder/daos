from daos.base import BaseDatabaseRepository as Base
from daos.internal.news_article.html_doc_index.model import NewsArticleHtmlDocumentIndexModel as Model


class NewsArticleHtmlDocumentIndexRepository(Base):
    def __init__(self):
        super().__init__('postgresql://postgres:root@localhost:5432/postgres', Model)
