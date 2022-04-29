from sqlalchemy import Column, String

from daos.abstracts.database.base import Model


class RssEntrySource(Model):
    __tablename__ = 'rss_entry_sources'

    name = Column(String)
