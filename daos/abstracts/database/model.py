from abc import ABC
from datetime import datetime

from peewee import (
    PostgresqlDatabase,
    BigIntegerField,
    DateTimeField
)

from . import config
from ..model import BaseModel

database = PostgresqlDatabase(config.POSTGRESQL_DBNAME)


class BaseDBModel(BaseModel, ABC):
    id = BigIntegerField(primary_key=True)
    created_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(default=datetime.now())

    class Meta:
        database = database
