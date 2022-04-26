from sqlalchemy import Column, DateTime, String, Integer, Boolean

from daos.abstracts.database.base import Model


class DocumentIndexEntry(Model):
    __tablename__ = 'document_index'

    scraped_at = Column(DateTime(True))
    url = Column(String)
    session_id = Column(String)
    ms_elapsed_on_webpage = Column(Integer)
    page_changes_observed = Column(Integer)
    document_path = Column(String)
