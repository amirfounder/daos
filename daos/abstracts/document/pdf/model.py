from typing import Optional

from ..model import DocumentModel as Base


class PdfDocumentModel(Base):
    filetype = '.pdf'
    read_mode = 'rb'
    write_mode = 'wb'

    def __init__(self, path: Optional[str] = None, *args, **kwargs):
        super().__init__(path, read_mode='rb', write_mode='wb', *args, **kwargs)
