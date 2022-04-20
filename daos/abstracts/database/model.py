import datetime
from typing import Dict

from inflector import Inflector

from sqlalchemy import Integer, Column, DateTime
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.orm import declared_attr

from .config import Base, MetaData

from ..model import BaseModel


class BaseDBModel(AbstractConcreteBase, BaseModel, Base):
    __abstract__ = True

    __tablename__: str

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(True), default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(True), default=datetime.datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__()
        columns = self.get_columns()
        for k, v in kwargs.items():
            if k in columns:
                setattr(self, k, v)

    @classmethod
    def get_columns(cls) -> Dict[str, Column]:
        return {c.name: c for c in MetaData.tables.get(cls.__tablename__).columns}

    # noinspection PyMethodParameters
    @declared_attr
    def __tablename__(cls):
        name = Inflector().underscore(cls.__name__)

        base: str = name
        suffix: str

        if name.endswith('y'):
            base = name[-1]
            suffix = 'ies'
        elif name.endswith('s'):
            suffix = 'es'
        else:
            suffix = 's'

        return f'{base}{suffix}'

    def dict(self):
        return {n: v for n in self.get_columns() if (v := getattr(self, n))}
