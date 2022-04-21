from daos.abstracts.document.pdf.repository import BasePdfDocumentRepository as Repository
from daos.abstracts.document.pdf.model import PdfDocumentModel as Model
from daos.internal.paths import GoogleSearchResults


class GoogleSearchResultsPdfDocumentRawHtmlRepository(Repository[Model]):
    def __init__(self):
        super().__init__(Model, GoogleSearchResults.RAW_HTML_PDF.value)


class GoogleSearchResultsPdfDocumentHtmlOnlyRepository(Repository[Model]):
    def __init__(self):
        super().__init__(Model, GoogleSearchResults.HTML_ONLY_PDF.value)
