from sqlalchemy import Column, DateTime, String, Integer, ForeignKey

from .rss_entry_sources import RssEntrySource

from daos.abstracts.database.base import Model


class RssEntryJsonFileIndexEntry(Model):
    __tablename__ = 'rss_entry_json_file_index'

    retrieved_at = Column(DateTime(True))
    source_id = Column(Integer, ForeignKey(RssEntrySource.id))
    file_path = Column(String)
