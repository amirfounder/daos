from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Boolean

from .rss_entry_sources import RssEntrySource

from daos.abstracts.database.base import Model
from .scraped_html_file_index import ScrapedHtmlFileIndexEntry


class RssEntryIndexEntry(Model):
    __tablename__ = 'rss_entry_index'

    retrieved_at = Column(DateTime(True))
    source_id = Column(Integer, ForeignKey(RssEntrySource.id))
    scraped_html_file_index_entry_id = Column(Integer, ForeignKey(ScrapedHtmlFileIndexEntry.id))
    has_been_scraped = Column(Boolean, default=False, nullable=False)
    file_path = Column(String)
    url = Column(String, unique=True)
