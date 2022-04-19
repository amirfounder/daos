import datetime

from sqlalchemy import Column, BigInteger, DateTime, String

from daos.base import BaseDatabaseModel as Base


class NewsArticleHtmlDocumentIndexModel(Base):
    __tablename__ = 'news_article_html_document_index'

    retrieved_from_web_at = Column(DateTime(True), default=datetime.datetime.utcnow)
    document_id = Column(BigInteger)
    document_format = Column(String)

    raw_version_document_path = Column(String)
    html_only_version_document_path = Column(String)
    no_js_version_document_path = Column(String)

    is_raw_version_stored = Column(String)
    is_html_only_version_stored = Column(String)
    is_no_js_version_stored = Column(String)

    source_url = Column(String)
    search_keywords = Column(String)
