import datetime

from sqlalchemy import Column, BigInteger, DateTime, String

from daos.base import BaseDatabaseModel


class NewsArticleHtmlDocumentIndexModel(BaseDatabaseModel):
    retrieved_from_web_at = Column(DateTime(True), default=datetime.datetime.utcnow)
    document_id = Column(BigInteger)
    document_format = Column(String)
    document_path = Column(String)
    source_url = Column(String)
    search_keywords = Column(String)
