from daos.abstracts.document.pdf.repository import BasePdfDocumentRepository as Repository
from daos.abstracts.document.pdf.model import PdfDocumentModel as Model
from daos.internal.paths import Paths


class RawHtmlPdfDocumentRepository(Repository[Model]):
    def __init__(self): super().__init__(Model, Paths.RAW_HTML_PDF.value)


class HtmlOnlyPdfDocumentRepository(Repository[Model]):
    def __init__(self): super().__init__(Model, Paths.HTML_ONLY_PDF.value)
