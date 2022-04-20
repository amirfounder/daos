from daos.abstracts.document.html.model import BaseHtmlDocModel as DocBase
from daos.internal.abstracts.doc_index_model import BaseHtmlDocIndexModel


class GoogleSearchResultsHtmlDocumentNoJSModel(DocBase):
    ...

class GoogleSearchResultsHtmlDocumentRawModel(DocBase):
    ...

class GoogleSearchResultsHtmlDocumentHtmlOnlyModel(DocBase):
    ...

class GoogleSearchResultsHtmlDocumentIndexModel(BaseHtmlDocIndexModel):
    ...
