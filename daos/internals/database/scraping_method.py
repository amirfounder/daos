from sqlalchemy import Column, String

from daos.abstracts.database.base import Model


# noinspection PyUnresolvedReferences
class ScrapingMethod(Model):
    __tablename__ = 'scraping_method_index'

    name = Column(String)
