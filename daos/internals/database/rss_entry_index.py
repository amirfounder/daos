from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Boolean

from .rss_entry_sources import RssEntrySource

from daos.abstracts.database.base import Model


class RssEntryIndexEntry(Model):
    __tablename__ = 'rss_entry_index'

    retrieved_at = Column(DateTime(True))
    source_id = Column(Integer, ForeignKey(RssEntrySource.id))
    file_path = Column(String)
    url = Column(String, unique=True)
    has_been_scraped = Column(Boolean, default=False)
