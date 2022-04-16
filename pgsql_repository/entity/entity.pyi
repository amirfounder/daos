import datetime
from typing import Any, Dict, List, Callable

from sqlalchemy import Column, BigInteger


class Base:
    __tablename__: str
    id: Column(BigInteger, primary_key=True)
    created_at: datetime.datetime
    updated_at: datetime.datetime
    """
    Entity base class
    """

    # def __init__(self, **kwargs): ...

    def as_dict(self) -> Dict[str, Any]:
        """
        Returns the dictionary representation of the object
        :return:
        """
        ...

    def get_columns(self) -> Dict[str, Column]:
        """
        :return:
        """