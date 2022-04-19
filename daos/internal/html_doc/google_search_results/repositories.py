from daos.base.document.html.repository import BaseHtmlDocumentRepository as Base
from daos.base.database.repository import BaseDatabaseRepository
from daos.internal.paths import Paths

from .models import (
    GoogleSearchResultsHtmlDocumentNoJSModel as NoJsModel,
    GoogleSearchResultsHtmlDocumentHtmlOnlyModel as HtmlOnlyModel,
    GoogleSearchResultsHtmlDocumentRawModel as RawModel,
    GoogleSearchResultsHtmlDocumentIndexModel as IndexModel
)


class GoogleSearchResultsHtmlDocumentNoJsRepository(Base[NoJsModel]):
    def __init__(self):
        super().__init__(
            model=NoJsModel,
            path=Paths.GOOGLE_SEARCH_RESULTS_NO_JS_DIR_PATH.value
        )


class GoogleSearchResultsHtmlDocumentHtmlOnlyRepository(Base[HtmlOnlyModel]):
    def __init__(self):
        super().__init__(
            model=HtmlOnlyModel,
            path=Paths.GOOGLE_SEARCH_RESULTS_HTML_ONLY_DIR_PATH.value
        )


class GoogleSearchResultsHtmlDocumentRawRepository(Base[RawModel]):
    def __init__(self):
        super().__init__(
            model=RawModel,
            path=Paths.GOOGLE_SEARCH_RESULTS_RAW_DIR_PATH.value
        )


class GoogleSearchResultsHtmlDocumentIndexRepository(BaseDatabaseRepository[IndexModel]):
    def __init__(self):
        super().__init__(IndexModel)
