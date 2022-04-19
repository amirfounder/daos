from typing import Dict

from daos.base import BaseFilter as Base
from .models import GoogleSearchResultsHtmlDocumentIndexModel as Model


class GoogleSearchResultsHtmlDocumentIndexFilter(Base[Model]):
    def __init__(self, params: Dict):
        super().__init__(Model, params)
