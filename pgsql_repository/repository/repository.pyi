from typing import TypeVar, Generic, Callable, Optional, List, Any

from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from pgsql_repository import Pageable, PagedResult
from pgsql_repository.core import Base, Metadata
from pgsql_repository.repository import SessionBuilder
from pgsql_repository.repository.repository import SchemaLoader

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
    schema_loader: SchemaLoader
    metadata: Metadata
    """
    Base repository containing default CRUD methods
    """

    def __init__(self, connection_string: str, entity: Base, metadata: Optional[Metadata] = Metadata):
        """
        Initializes the repository
        :param connection_string: The connection string (i.e. postgresql://postgres:root@localhost:5432/postgres)
        """
        ...

    def _paginate_select(self, stmt: Any, pageable: Pageable) -> Any:
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

    def get_all(self) -> List[T] | PagedResult[T]:
        ...

    def _get_all_by_pageable(self, session: Session, pageable: Pageable):
        ...
