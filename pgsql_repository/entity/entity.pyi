import datetime

from sqlalchemy import Column, BigInteger


class Base:
    id: Column(BigInteger, primary_key=True)
    created_at: datetime.datetime
    updated_at: datetime.datetime
    """
    Entity base class
    """

    def as_dict(self):
        """
        Returns the dictionary representation of the object
        :return:
        """
        ...
