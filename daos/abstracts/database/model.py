import datetime
from typing import Dict

from sqlalchemy import Integer, Column, DateTime, MetaData
from sqlalchemy.ext.declarative import AbstractConcreteBase

from .config import Base

from ..model import BaseModel


class BaseDatabaseModel(AbstractConcreteBase, BaseModel, Base):
    __abstract__ = True
    __tablename__: str
    metadata: MetaData

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(True), default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(True), default=datetime.datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__()
        self.created_at = datetime.datetime.now(datetime.timezone.utc)
        self.created_at = datetime.datetime.now(datetime.timezone.utc)
        for k, v in kwargs.items():
            if k in (columns := self.get_columns()):
                if columns.get(k).primary_key:
                    raise Exception('Cannot assign primary key.')
                setattr(self, k, v)

    @classmethod
    def get_columns(cls) -> Dict[str, Column]:
        return {c.name: c for c in cls.metadata.tables.get(cls.__tablename__).columns}

    def dict(self):
        return {n: v for n in self.get_columns() if (v := getattr(self, n, None))}
