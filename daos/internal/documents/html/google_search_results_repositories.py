from daos.abstracts.document.html.repository import BaseHtmlDocRepository as DocBase
from daos.abstracts.database.repository import BaseDBRepository as DBBase
from daos.internal.paths import Paths

from .google_search_results_models import (
    GoogleSearchResultsHtmlDocumentIndexModel as Index,
    GoogleSearchResultsHtmlDocumentRawModel as Raw,
    GoogleSearchResultsHtmlDocumentHtmlOnlyModel as HtmlOnly,
    GoogleSearchResultsHtmlDocumentNoJSModel as NoJs
)


class GoogleSearchResultsHtmlDocumentNoJSRepository(DocBase):
    def __init__(self):
        super().__init__(NoJs, Paths.GOOGLE_SEARCH_RESULTS_NO_JS_DIR_PATH.value)

class GoogleSearchResultsHtmlDocumentRawRepository(DocBase):
    def __init__(self):
        super().__init__(Raw, Paths.GOOGLE_SEARCH_RESULTS_RAW_DIR_PATH.value)

class GoogleSearchResultsHtmlDocumentHtmlOnlyRepository(DocBase):
    def __init__(self):
        super().__init__(HtmlOnly, Paths.GOOGLE_SEARCH_RESULTS_HTML_ONLY_DIR_PATH.value)

class GoogleSearchResultsHtmlDocumentIndexRepository(DBBase):
    def __init__(self):
        super().__init__(Index)
