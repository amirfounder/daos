from typing import Dict

from daos.base import BaseFilterable as Base
from .model import NewsArticleHtmlDocumentIndexModel as Model


class NewsArticleHtmlDocumentIndexFilter(Base):
    def __init__(self, params: Dict):
        super().__init__(Model, params)
