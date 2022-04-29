from sqlalchemy import Column, String, Integer, ForeignKey

from daos.abstracts.database.base import Model

from .rss_entry_sources import RssEntrySource


class RssFeedUrl(Model):
    __tablename__ = 'rss_feed_urls'

    source_id = Column(Integer, ForeignKey(RssEntrySource.id))
    name = Column(String)
    url = Column(String)
