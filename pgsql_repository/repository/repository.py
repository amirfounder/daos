from __future__ import annotations
from typing import Generic, TypeVar, List, Optional, Any

from sqlalchemy import select, insert, func, Column
from sqlalchemy.engine import create_engine, Engine
from sqlalchemy.orm import Session

from pgsql_repository.core import Metadata
from pgsql_repository.pagination.pageable import Pageable
from pgsql_repository.pagination.pagedresult import PagedResult
from pgsql_repository.filtering.filterable import Filterable
from pgsql_repository.entity import Base as Entity
from pgsql_repository.sessions import SessionBuilder

T = TypeVar('T')


class SchemaLoader:
    def __init__(
            self,
            model: Entity,
            metadata: Metadata,
            engine: Engine,
            session_builder: SessionBuilder
    ):
        self.model = model
        self.metadata = metadata
        self.engine = engine
        self.session_builder = session_builder

    def _get_pgsql_columns_by_table(self, name: str):
        with self.session_builder.open() as session:
            return session.execute(
                '''
                select column_name
                from information_schema.columns
                where table_name = '{table}'
                and table_schema = 'public'
                '''.format(table=name)
            ).scalars().all()

    def _remove_columns(self, table: str, columns: List[str]):
        drop_column_statements = ', '.join([f'DROP COLUMN {c}' for c in columns])
        alter_table_statement = f'ALTER TABLE {table} {drop_column_statements};'
        with self.session_builder.open() as session:
            session.execute(alter_table_statement)

    def _create_columns(self, table: str, columns: List[Column]):
        add_column_statements = ', '.join([f'ADD COLUMN {c.name} {c.type.compile()}' for c in columns])
        alter_table_statement = f'ALTER TABLE {table} {add_column_statements}'
        with self.session_builder.open() as session:
            session.execute(alter_table_statement)

    def load(self):
        for table in self.metadata.tables:
            # noinspection PyArgumentList
            model_columns_map = self.model.get_columns()
            model_columns = [k for k in model_columns_map]
            pgsql_columns = self._get_pgsql_columns_by_table(table)

            columns_to_remove = [c for c in pgsql_columns if c not in model_columns]
            columns_to_create = [model_columns_map.get(c) for c in model_columns if c not in pgsql_columns]

            if columns_to_create:
                self._create_columns(table, columns_to_create)
            if columns_to_remove:
                self._remove_columns(table, columns_to_remove)


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

    def create_in_batch(self, _: Session, models: List[T]) -> List[T]:
        return [self.create(m) for m in models]

    def update(self, model: T) -> T:
        with self.session_builder.open() as session:
            return session.query(T).filter(T.id == model.id).update(model.__dict__)

    def update_in_batch(self, _: Session, models: T) -> List[T]:
        return [self.update(m) for m in models]

    def delete(self, model_id: int) -> None:
        with self.session_builder.open() as s:
            s.query(T).filter(T.id == model_id).delete()

    def delete_in_batch(self, model_ids: List[int]) -> None:
        [self.delete(m) for m in model_ids]
