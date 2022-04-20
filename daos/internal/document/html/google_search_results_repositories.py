from daos.abstracts.document.html.repository import BaseHtmlDocRepository as DocBase
from daos.abstracts.database.repository import BaseDBRepository as DBBase
from daos.internal.paths import Paths


class GoogleSearchResultsHtmlDocumentNoJSRepository(DocBase):
    def __init__(self):
        super().__init__(Paths.GOOGLE_SEARCH_RESULTS_NO_JS_DIR_PATH.value)

class GoogleSearchResultsHtmlDocumentRawRepository(DocBase):
    def __init__(self):
        super().__init__(Paths.GOOGLE_SEARCH_RESULTS_RAW_DIR_PATH.value)

class GoogleSearchResultsHtmlDocumentHtmlOnlyRepository(DocBase):
    def __init__(self):
        super().__init__(Paths.GOOGLE_SEARCH_RESULTS_HTML_ONLY_DIR_PATH.value)

class GoogleSearchResultsHtmlDocumentIndexRepository(DBBase): ...
