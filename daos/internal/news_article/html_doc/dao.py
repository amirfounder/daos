from daos.base.document.html.dao import BaseHtmlDocumentDao
from daos.internal.news_article.html_doc.model import NewsArticleHtmlDocumentModel as Model


class NewsArticleHtmlDocumentDao(BaseHtmlDocumentDao):
    def __init__(self):
        super().__init__(Model, 'C:/ai-ml-project/data/html/news-articles')
