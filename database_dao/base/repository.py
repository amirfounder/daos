from __future__ import annotations

from datetime import timezone, datetime
from typing import List, Optional, Type

from sqlalchemy import select, insert, update, delete
from sqlalchemy.engine import create_engine

from database_dao.core import Metadata
from database_dao.extensions.pagination.pageable import BasePageable
from database_dao.extensions.pagination.pagedresult import PagedResult
from database_dao.extensions.filtering.filterable import BaseFilterable
from database_dao.model import BaseModel
from database_dao.base.schema_loader import SchemaLoader
from database_dao.base.sessions import SessionBuilder


class BaseModelRepository:
    def __init__(self, connection_string: str, model: Type[BaseModel], metadata: Optional[Metadata] = Metadata):
        self.model = model
        self.connection_string = connection_string
        self.metadata = metadata

        self.engine = create_engine(self.connection_string, future=True)
        self.session_builder = SessionBuilder(self.engine)
        self.schema_loader = SchemaLoader(self.model, self.metadata, self.session_builder)
        self.schema_loader.load()

    def get_by_id(self, _id: int) -> BaseModel:
        with self.session_builder.open() as session:
            return session.get(self.model, _id)

    def get_by_id_in_batch(self, ids: List[int]):
        with self.session_builder.open() as session:
            return session.execute(select(self.model).where(self.model.id.in_(ids))).scalars().all()
    
    def get_all(self, pageable: Optional[BasePageable] = None) -> List[BaseModel]:
        with self.session_builder.open() as session:
            sql_query = select(self.model)
            if pageable:
                sql_query = pageable.apply(sql_query)
            return session.execute(sql_query).scalars().all()

    def get_all_by_filterable(self, filterable: BaseFilterable, pageable: Optional[BasePageable] = None)\
            -> List[BaseModel] | PagedResult[BaseModel]:
        with self.session_builder.open() as session:
            sql_query = select(self.model)
            sql_query = filterable.apply(sql_query)
            if pageable:
                sql_query = pageable.apply(sql_query)
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
            pk = session.execute(insert(self.model).values(**instance.dict())).inserted_primary_key
            return session.get(self.model, pk)

    def create_in_batch(self, instances: List[BaseModel]) -> None:
        for instance in instances:
            now = datetime.now(timezone.utc)
            instance.created_at = now
            instance.updated_at = now
        with self.session_builder.open() as session:
            session.execute(insert(self.model).values([instance.dict() for instance in instances]))

    def update(self, instance: BaseModel) -> BaseModel:
        instance.updated_at = datetime.now(timezone.utc)
        with self.session_builder.open() as session:
            return session.execute(update(self.model).where(self.model.id == instance.id).values(instance.dict()))

    def update_in_batch(self, instances: List[BaseModel]) -> None:
        for instance in instances:
            instance.updated_at = datetime.now(timezone.utc)
        with self.session_builder.open() as session:
            for instance in instances:
                session.execute(update(self.model).where(self.model.id == instance.id).values(instance.dict()))

    def delete(self, _id: int) -> None:
        with self.session_builder.open() as session:
            session.execute(delete(self.model).where(self.model.id == _id))

    def delete_in_batch(self, ids: List[int]) -> None:
        with self.session_builder.open() as session:
            session.execute(delete(self.model).where(self.model.id in ids))
