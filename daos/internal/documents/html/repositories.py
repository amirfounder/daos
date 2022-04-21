from daos.abstracts.document.html.repository import BaseHtmlDocRepository as Repository
from daos.abstracts.document.html.model import HtmlDocumentModel as Model
from daos.internal.paths import Paths


class RawHtmlDocumentRepository(Repository[Model]):
    def __init__(self): super().__init__(Model, Paths.raw_html.value)


class HtmlOnlyHtmlDocumentRepository(Repository[Model]):
    def __init__(self): super().__init__(Model, Paths.html_only.value)
