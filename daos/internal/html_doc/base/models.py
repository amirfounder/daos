from sqlalchemy import Column, DateTime, BigInteger, String, Boolean

from daos.base import BaseDatabaseModel as Base


class BaseNewsArticleHtmlDocumentIndexModel(Base):

    retrieved_from_web_at = Column(DateTime(True))
    document_id = Column(BigInteger)
    document_format = Column(String)

    raw_version_document_path = Column(String)
    html_only_version_document_path = Column(String)
    no_js_version_document_path = Column(String)

    is_raw_version_stored = Column(Boolean, default=False)
    is_html_only_version_stored = Column(Boolean, default=False)
    is_no_js_version_stored = Column(Boolean, default=False)

    url = Column(String)
