from abc import ABC
from typing import Optional

from bs4 import BeautifulSoup

from daos.base.document.abstract import BaseDocumentModel


class BaseHtmlDocumentModel(BaseDocumentModel, ABC):
    def __init__(self, path: str, contents: Optional[str] = None):
        super().__init__(path, contents)
        self.soup: BeautifulSoup

    def as_soup(self):
        return BeautifulSoup(self.contents, 'html.parser')
