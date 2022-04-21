from daos.abstracts.document.pdf.repository import BasePdfDocumentRepository as Repository
from daos.abstracts.document.pdf.model import PdfDocumentModel as Model
from daos.internal.paths import Paths


class RawHtmlPdfDocumentRepository(Repository[Model]):
    def __init__(self): super().__init__(Model, Paths.raw_html_pdfs.value)


class HtmlOnlyPdfDocumentRepository(Repository[Model]):
    def __init__(self): super().__init__(Model, Paths.html_only_pdfs.value)
