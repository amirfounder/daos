from daos.abstracts.document.html.repository import BaseHtmlDocRepository as Repository
from daos.abstracts.document.html.model import HtmlDocumentModel as Model
from daos.internal.paths import GoogleSearchResults


class GoogleSearchResultsHtmlDocumentNoJSRepository(Repository[Model]):
    def __init__(self): super().__init__(Model, GoogleSearchResults.NO_JS.value)


class GoogleSearchResultsHtmlDocumentRawHtmlRepository(Repository[Model]):
    def __init__(self): super().__init__(Model, GoogleSearchResults.RAW_HTML.value)


class GoogleSearchResultsHtmlDocumentHtmlOnlyRepository(Repository[Model]):
    def __init__(self): super().__init__(Model, GoogleSearchResults.HTML_ONLY.value)
