from abc import ABC
from typing import Optional

from bs4 import BeautifulSoup

from daos.base.document.base import BaseDocumentModel


class BaseHtmlDocumentModel(BaseDocumentModel, ABC):
    def __init__(self, contents: Optional[str] = None):
        super().__init__(contents)
        self.soup: Optional[BeautifulSoup] = None

    def load_soup(self):
        self.soup = BeautifulSoup(self.contents, 'html.parser')
