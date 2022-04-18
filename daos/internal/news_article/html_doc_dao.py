from daos.base.document.html import BaseHtmlDocumentDao


class NewsArticleHtmlDocumentDao(BaseHtmlDocumentDao):
    def __init__(self):
        super().__init__('C:/ai-ml-project/data/html/news-articles')

