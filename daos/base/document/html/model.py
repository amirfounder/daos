from abc import ABC
from typing import Optional

from bs4 import BeautifulSoup

from daos.base.document.base import BaseDocumentModel


class BaseHtmlDocumentModel(BaseDocumentModel, ABC):
    def __init__(self, contents: Optional[str] = None, path: Optional[str] = None):
        super().__init__(contents, path)
        self.soup: Optional[BeautifulSoup] = None

    def as_soup(self):
        if not self.soup:
            self.soup = BeautifulSoup(self.contents, 'html.parser')
        return self.soup
