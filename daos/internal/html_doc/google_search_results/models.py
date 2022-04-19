from sqlalchemy import Column, String

from daos.base.document.html.model import BaseHtmlDocumentModel as DocumentBase
from daos.internal.html_doc.base.models import BaseHtmlDocumentIndexModel as DatabaseBase


class GoogleSearchResultsHtmlDocumentNoJSModel(DocumentBase):
    ...


class GoogleSearchResultsHtmlDocumentRawModel(DocumentBase):
    ...


class GoogleSearchResultsHtmlDocumentHtmlOnlyModel(DocumentBase):
    ...


class GoogleSearchResultsHtmlDocumentIndexModel(DatabaseBase):
    __tablename__ = 'google_results_html_document_indices'

    search_keywords = Column(String)
