from daos.abstracts.document.pdf.repository import BasePdfDocumentRepository as Repository
from daos.abstracts.document.pdf.model import PdfDocumentModel as Model
from daos.internal.paths import Paths


class RawHtmlPdfDocumentRepository(Repository[Model]):
    def __init__(self): super().__init__(Model, Paths.raw_html_pdfs.value)


class ProcessedHtmlV1PdfDocumentRepository(Repository[Model]):
    def __init__(self): super().__init__(Model, Paths.processed_html_v1_pdfs.value)
