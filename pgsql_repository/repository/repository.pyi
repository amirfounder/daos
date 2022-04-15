from typing import TypeVar, Generic, Callable

from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from pgsql_repository import Pageable
from pgsql_repository.core import Base, Metadata
from pgsql_repository.repository import SessionBuilder

T = TypeVar('T')


def session_wrapper(func: Callable):
    """
    Wraps a method of a Repository type to inject its session as the first positional argument.
    :type func: object The function to wrap
    """
    ...


class Repository(Generic[T]):
    entity: Base
    connection_string: str
    engine: Engine
    session_builder: SessionBuilder
    metadata: Metadata
    """
    Base repository containing default CRUD methods
    """

    def __init__(self, entity: Base, connection_string: str):
        """
        Initializes the repository
        :param connection_string: The connection string (i.e. postgresql://postgres:root@localhost:5432/postgres)
        """
        ...

    def _emit_table_ddl(self):
        ...

    def create(self, model: T) -> T:
        """
        Creates an instance of the entity in the database
        :param model: The entity to create
        :return: The entity created
        """
        ...

    def get_by_id(self, id: int) -> T:
        ...

    def _get_all_by_pageable(self, session: Session, pageable: Pageable):
        ...
