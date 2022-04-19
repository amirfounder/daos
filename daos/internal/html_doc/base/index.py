from typing import Dict

from daos.base import BaseDatabaseRepository as Repository
from daos.base import BaseFilter as Filter


class NewsArticleHtmlDocumentIndexRepository(Repository[BaseNewsArticleHtmlDocumentIndexModel]):
    def __init__(self):
        super().__init__(BaseNewsArticleHtmlDocumentIndexModel)


class NewsArticleHtmlDocumentIndexFilter(Filter):
    def __init__(self, params: Dict):
        super().__init__(BaseNewsArticleHtmlDocumentIndexModel, params)
