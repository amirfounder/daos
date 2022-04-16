from __future__ import annotations

from datetime import timezone, datetime
from typing import List, Optional, Any, Type

from sqlalchemy import func, select, insert, update, delete
from sqlalchemy.engine import create_engine

from pgsql_repository.core import Metadata
from pgsql_repository.extensions.pagination.pageable import Pageable
from pgsql_repository.extensions.pagination.pagedresult import PagedResult
from pgsql_repository.filtering.filterable import BaseFilterable
from pgsql_repository.model import BaseModel
from pgsql_repository.repository.schema_loader import SchemaLoader
from pgsql_repository.repository.sessions import SessionBuilder


class BaseModelRepository:
    def __init__(self, connection_string: str, model: Type[BaseModel], metadata: Optional[Metadata] = Metadata):
        self.model = model
        self.connection_string = connection_string
        self.metadata = metadata
        self.engine = create_engine(self.connection_string, future=True)
        self.session_builder = SessionBuilder(self.engine)
        self.schema_loader = SchemaLoader(self.model, self.metadata, self.engine, self.session_builder)
        self.schema_loader.load()

    # noinspection PyMethodMayBeStatic
    def _paginate_select(self, sql_query: Any, p: Pageable) -> BaseModel:
        return sql_query.offset(p.page * p.size).limit(p.size)

    def get_by_id(self, _id: int) -> BaseModel:
        with self.session_builder.open() as session:
            return session.get(self.model, _id)

    def get_by_id_in_batch(self, ids: List[int]):
        with self.session_builder.open() as session:
            return session.execute(select(self.model).where(self.model.id.in_(ids))).scalars().all()
    
    def get_all(self, pageable: Optional[Pageable] = None) -> List[BaseModel]:
        with self.session_builder.open() as session:
            sql_query = select(self.model)
            if pageable:
                sql_query = self._paginate_select(sql_query, pageable)
            return session.execute(sql_query).scalars().all()

    def get_all_by_filterable(self, filterable: BaseFilterable, pageable: Optional[Pageable] = None)\
            -> List[BaseModel] | PagedResult[BaseModel]:
        with self.session_builder.open() as session:
            sql_query = select(self.model)
            for key, value in filterable.filters.items():
                sql_query = sql_query.where(
                    getattr(self.model, key) == (
                        func.lower(value) if
                        isinstance(value, str)
                        else value
                    )
                )
            if pageable:
                sql_query = self._paginate_select(sql_query, pageable)
            return session.execute(sql_query).scalars().all()

    def get_distinct_by_column(self, column_name: str):
        with self.session_builder.open() as session:
            if column_name not in self.model.get_columns():
                raise Exception(f'Column not found : {self.model} - {column_name}.')
            return session.execute(select(getattr(self.model, column_name)).distinct().scalars().all())

    def create(self, instance: BaseModel) -> BaseModel:
        now = datetime.now(timezone.utc)
        instance.created_at = now
        instance.updated_at = now
        with self.session_builder.open() as session:
            pk = session.execute(insert(self.model).values(**instance.to_dict())).inserted_primary_key
            return session.get(self.model, pk)

    def create_in_batch(self, instances: List[BaseModel]) -> None:
        for instance in instances:
            now = datetime.now(timezone.utc)
            instance.created_at = now
            instance.updated_at = now
        with self.session_builder.open() as session:
            session.execute(insert(self.model).values([instance.to_dict() for instance in instances]))

    def update(self, instance: BaseModel) -> BaseModel:
        instance.updated_at = datetime.now(timezone.utc)
        with self.session_builder.open() as session:
            return session.execute(update(self.model).where(self.model.id == instance.id).values(instance.to_dict()))

    def update_in_batch(self, instances: List[BaseModel]) -> None:
        for instance in instances:
            instance.updated_at = datetime.now(timezone.utc)
        with self.session_builder.open() as session:
            for instance in instances:
                session.execute(update(self.model).where(self.model.id == instance.id).values(instance.to_dict()))

    def delete(self, _id: int) -> None:
        with self.session_builder.open() as session:
            session.execute(delete(self.model).where(self.model.id == _id))

    def delete_in_batch(self, ids: List[int]) -> None:
        with self.session_builder.open() as session:
            session.execute(delete(self.model).where(self.model.id in ids))
