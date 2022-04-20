from typing import Optional

from bs4 import BeautifulSoup

from ..model import DocumentModel


class HtmlDocumentModel(DocumentModel):
    def __init__(self, path: Optional[str] = None, *args, **kwargs):
        super().__init__(path, *args, **kwargs)
        self.soup: Optional[BeautifulSoup] = None

    def load_soup(self):
        self.soup = BeautifulSoup(self.contents, 'html.parser')
