from datetime import datetime


from sqlalchemy import Column, DateTime, BigInteger, String, Boolean

from daos.abstracts.database.model import BaseDBModel
from daos.abstracts.database.config import Base


class HtmlDocumentIndexItem(BaseDBModel, Base):

    retrieved_from_web_at = Column(DateTime(True), default=datetime.utcnow)
    document_id = Column(BigInteger)
    document_format = Column(String)

    raw_version_document_path = Column(String)
    html_only_version_document_path = Column(String)
    no_js_version_document_path = Column(String)
    pdf_version_document_path = Column(String)

    is_raw_version_stored = Column(Boolean, default=False)
    is_html_only_version_stored = Column(Boolean, default=False)
    is_no_js_version_stored = Column(Boolean, default=False)
    is_pdf_version_stored = Column(Boolean, default=False)

    url = Column(String)
