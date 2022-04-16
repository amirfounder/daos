from __future__ import annotations
from typing import Generic, TypeVar, List, Optional, Any

from sqlalchemy import select, insert, func, update, delete
from sqlalchemy.engine import create_engine

from pgsql_repository.core import Metadata
from pgsql_repository.pagination.pageable import Pageable
from pgsql_repository.pagination.pagedresult import PagedResult
from pgsql_repository.filtering.filterable import Filterable
from pgsql_repository.entity import Entity
from pgsql_repository.repository.schema_loader import SchemaLoader
from pgsql_repository.repository.sessions import SessionBuilder

T = TypeVar('T')


class Repository(Generic[T]):
    def __init__(self, connection_string: str, entity: Entity, metadata: Optional[Metadata] = Metadata):
        self.entity = entity
        self.connection_string = connection_string
        self.metadata = metadata
        self.engine = create_engine(self.connection_string, future=True)
        self.session_builder = SessionBuilder(self.engine)
        self.schema_loader = SchemaLoader(self.entity, self.metadata, self.engine, self.session_builder)
        self.schema_loader.load()

    # noinspection PyMethodMayBeStatic
    def _paginate_select(self, stmt: Any, p: Pageable) -> Any:
        return stmt.offset(p.page * p.size).limit(p.size)

    def _filter_select(self, stmt: any, f: Filterable) -> Any:
        for k, v in f.filters.items():
            stmt = stmt.where(getattr(self.entity, k) == func.lower(v) if isinstance(v, str) else v)

    def get_by_id(self, _id: int) -> T:
        with self.session_builder.open() as session:
            return session.get(self.entity, _id)

    def get_by_id_in_batch(self, ids: List[int]):
        with self.session_builder.open() as session:
            return session.execute(select(self.entity).where(self.entity.id in ids)).scalars().all()
    
    def get_all(self, pageable: Optional[Pageable] = None) -> List[T]:
        with self.session_builder.open() as session:
            stmt = select(self.entity)
            if pageable:
                stmt = self._paginate_select(stmt, pageable)
            return session.execute(stmt).scalars().all()

    def get_all_by_filterable(self, f: Filterable, p: Optional[Pageable] = None) -> List[T] | PagedResult[T]:
        with self.session_builder.open() as session:
            stmt = select(self.entity)
            stmt = self._filter_select(stmt, f)
            if p:
                stmt = self._paginate_select(stmt, p)
            return session.execute(stmt).scalars().all()

    def get_distinct_by_column(self, column: str):
        with self.session_builder.open() as session:
            if column not in self.entity.get_columns():
                raise Exception(f'Column not found : {self.entity} - {column}.')
            return session.execute(select(getattr(self.entity, column)).distinct().scalars().all())

    def create(self, model: T) -> T:
        with self.session_builder.open() as session:
            pk = session.execute(insert(self.entity).values(**model.to_dict())).inserted_primary_key
            return session.get(self.entity, pk)

    def create_in_batch(self, models: List[T]) -> None:
        with self.session_builder.open() as session:
            session.execute(insert(self.entity).values([m.to_dict() for m in models]))

    def update(self, model: T) -> T:
        with self.session_builder.open() as session:
            return session.query(T).filter(T.id == model.id).update(model.__dict__)

    def update_in_batch(self, models: T) -> None:
        with self.session_builder.open() as session:
            session.execute(update(self.entity).values([m.to_dict() for m in models]))

    def delete(self, _id: int) -> None:
        with self.session_builder.open() as s:
            s.execute(delete(self.entity).where(self.entity.id == _id))

    def delete_in_batch(self, ids: List[int]) -> None:
        with self.session_builder.open() as s:
            s.execute(delete(self.entity).where(self.entity.id in ids))
