from datetime import datetime

from peewee import (
    Model,
    DateTimeField
)

from ..model import BaseModel
from .config import database


class BaseDBModel(Model, BaseModel):
    created_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(default=datetime.now())

    class Meta:
        database = database
