from daos.abstracts.document.pdf.repository import BasePdfDocumentRepository as Repository
from daos.abstracts.document.pdf.model import PdfDocumentModel as Model
from daos.internal.paths import NewsArticles


class NewsArticlesPdfDocumentRawHtmlRepository(Repository[Model]):
    def __init__(self):
        super().__init__(Model, NewsArticles.RAW_HTML_PDF.value)


class NewsArticlesPdfDocumentHtmlOnlyRepository(Repository[Model]):
    def __init__(self):
        super().__init__(Model, NewsArticles.HTML_ONLY_PDF.value)
