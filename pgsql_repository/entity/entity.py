import datetime

from sqlalchemy import Integer, Column, DateTime

from pgsql_repository.core import Base


def init(self):
    # self.from_dict(kwargs)
    # noinspection PyArgumentList
    super(Base, self).__init__()
    self.created_at = datetime.datetime.now(datetime.timezone.utc)
    self.created_at = datetime.datetime.now(datetime.timezone.utc)


def as_dict(self):
    return {n: v for n in self.get_columns() if (v := getattr(self, n, None))}


def from_dict(self, kwargs):
    for k, v in kwargs.items():
        if k in (columns := self.get_columns()):
            # if columns.get(k).primary_key:
            #     raise Exception('Cannot assign primary key.')
            setattr(self, k, v)


def get_columns(self):
    return {c.name: c for c in self.metadata.tables.get(self.__tablename__).columns}


Base.__init__ = init

Base.as_dict = as_dict
Base.from_dict = from_dict
Base.get_columns = get_columns

Base.id = Column(Integer, primary_key=True)
Base.created_at = Column(DateTime(True), default=datetime.datetime.utcnow)
Base.updated_at = updated_at = Column(DateTime(True), default=datetime.datetime.utcnow)
