from __future__ import annotations

from datetime import timezone, datetime
from typing import List, Type, TypeVar, Generic

from sqlalchemy import select, insert, update, delete

from .filter import BaseFilter
from .schema_loader import SchemaLoader
from .session_context import SessionContext

T = TypeVar('T')

POSTGRESQL_CONNECTION_STRING = 'postgresql://postgres:root@localhost:5432/postgres'


class BaseDBRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model
        self.session = SessionContext
        self.schema_loader = SchemaLoader(self.model)
        self.schema_loader.load()

    def create(self, **kwargs):
        instance = self.model(**kwargs)
        return self.save(instance)

    def get(self, _id: int) -> T:
        with self.session() as session:
            return session.get(self.model, _id)

    def get_all(self) -> List[T]:
        with self.session() as session:
            sql_query = select(self.model)
            return session.execute(sql_query).scalars().all()

    def get_all_by_filter(self, _filter: BaseFilter) -> List[T]:
        with self.session() as session:
            sql_query = select(self.model)
            sql_query = _filter.apply(sql_query)
            return session.execute(sql_query).scalars().all()

    def save(self, instance: T) -> T:
        now = datetime.now(timezone.utc)
        instance.created_at = now
        instance.updated_at = now
        with self.session() as session:
            pk = session.execute(insert(self.model).values(instance.dict())).inserted_primary_key
            return session.get(self.model, pk)

    def update(self, instance: T) -> T:
        instance.updated_at = datetime.now(timezone.utc)
        with self.session() as session:
            return session.execute(update(self.model).where(self.model.id == instance.id).values(instance.dict()))

    def delete(self, _id: int) -> None:
        with self.session() as session:
            session.execute(delete(self.model).where(self.model.id == _id))
