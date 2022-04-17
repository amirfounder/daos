import datetime
from typing import Any, Dict, List, Callable

from sqlalchemy import Column, BigInteger

from database_dao.core import Metadata


class BaseModel:
    __tablename__: str
    id: Column(BigInteger, primary_key=True)
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata: Metadata
    """
    BaseModel base class
    """

    def __init__(self, **kwargs): ...

    def dict(self) -> Dict[str, Any]:
        """
        Returns the dictionary representation of the object
        :return:
        """
        ...

    def from_keywords(self, **kwargs):
        pass

    @classmethod
    def get_columns(cls) -> Dict[str, Column]:
        """
        :return:
        """