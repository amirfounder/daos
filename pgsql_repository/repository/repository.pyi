from typing import TypeVar, Generic, Callable, Optional, List, Any, Type

from sqlalchemy.engine import Engine

from pgsql_repository.model.model import BaseModel
from pgsql_repository.filtering import BaseFilterable
from pgsql_repository.pagination import Pageable, PagedResult
from pgsql_repository.core import Base, Metadata
from pgsql_repository.repository.sessions import SessionBuilder
from pgsql_repository.repository.schema_loader import SchemaLoader

T = TypeVar('T')


def session_wrapper(func: Callable):
    """
    Wraps a method of a BaseModelRepository type to inject its session as the first positional argument.
    :type func: object The function to wrap
    """
    ...


class BaseModelRepository:
    connection_string: str
    engine: Engine
    model: Type[BaseModel]
    metadata: Metadata
    session_builder: SessionBuilder
    schema_loader: SchemaLoader
    """
    Base repository containing default CRUD methods
    """

    def __init__(self, connection_string: str, model: BaseModel, metadata: Optional[Metadata] = Metadata):
        """
        Initializes the repository
        :param connection_string: The connection string (i.e. postgresql://postgres:root@localhost:5432/postgres)
        """
        ...

    def _filter_select(self, stmt: Any, filterable: BaseFilterable): ...

    def _paginate_select(self, stmt: Any, pageable: Pageable): ...

    def get_by_id(self, id: int) -> T:
        ...
    def get_by_id_in_batch(self, ids: List[int]) -> List[T]:
        ...

    def get_all(self, pageable: Optional[Pageable] = None) -> List[T] | PagedResult[T]:
        ...

    def get_all_by_filter(self, filterable: BaseFilterable, pageable: Optional[Pageable] = None) -> List[T] | PagedResult[T]:
        ...

    def get_distinct_by_column(self, column_name: str):
        ...

    def create(self, model: T) -> T:
        """
        Creates an instance of the model in the database
        :param model: The model to create
        :return: The model created
        """
        ...

    def create_in_batch(self, models: List[T]) -> None:
        ...

    def update(self, model: T) -> T:
        ...

    def update_in_batch(self, models: T) -> None:
        ...

    def delete(self, _id: int) -> None:
        ...

    def delete_in_batch(self, ids: List[int]) -> None:
        ...
