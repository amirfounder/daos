from typing import Optional

from bs4 import BeautifulSoup

from ..model import DocumentModel


class HtmlDocumentModel(DocumentModel):
    suffix = '.html'

    def __init__(self, path: Optional[str] = None):
        super().__init__(path)
        self.soup: Optional[BeautifulSoup] = None

    def load_soup(self):
        self.soup = BeautifulSoup(self.contents, 'html.parser')
