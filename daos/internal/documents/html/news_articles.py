from daos.abstracts.document.html.repository import BaseHtmlDocRepository as Repository
from daos.abstracts.document.html.model import HtmlDocumentModel as Model
from daos.internal.paths import NewsArticles


class NewsArticleHtmlDocumentNoJSRepository(Repository[Model]):
    def __init__(self):
        super().__init__(Model, NewsArticles.NO_JS.value)


class NewsArticleHtmlDocumentRawHtmlRepository(Repository[Model]):
    def __init__(self):
        super().__init__(Model, NewsArticles.RAW_HTML.value)


class NewsArticleHtmlDocumentHtmlOnlyRepository(Repository[Model]):
    def __init__(self):
        super().__init__(Model, NewsArticles.HTML_ONLY.value)
