from typing import Optional

from ..model import DocumentModel as Base


class PdfDocumentModel(Base):
    suffix = '.pdf'
    read_mode = 'rb'
    write_mode = 'wb'

    def __init__(self, path: Optional[str] = None):
        super().__init__(path)
