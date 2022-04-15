import datetime

from sqlalchemy import Integer, Column, DateTime

from pgsql_repository.core import Base as Entity


def init(self):
    # noinspection PyArgumentList
    super(Entity, self).__init__()
    self.created_at = datetime.datetime.now(datetime.timezone.utc)
    self.created_at = datetime.datetime.now(datetime.timezone.utc)


Entity.__init__ = init


def as_dict(self):
    return {x: y for x, y in self.__dict__.items() if not x.startswith('_')}


Entity.as_dict = as_dict

Entity.id = Column(Integer, primary_key=True)
Entity.created_at = Column(DateTime(True), default=datetime.datetime.utcnow)
Entity.updated_at = updated_at = Column(DateTime(True), default=datetime.datetime.utcnow)
