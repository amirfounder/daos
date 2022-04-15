from __future__ import annotations
from typing import Generic, TypeVar, List, Optional, Any

from sqlalchemy import select, insert, func
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session

from pgsql_repository.core import Metadata
from pgsql_repository.pagination.pageable import Pageable
from pgsql_repository.pagination.pagedresult import PagedResult
from pgsql_repository.filtering.filterable import Filterable
from pgsql_repository.entity import Base as Entity
from pgsql_repository.sessions import SessionBuilder

T = TypeVar('T')


class Repository(Generic[T]):
    def __init__(self, entity: Entity, connection_string: str):
        self.entity = entity
        self.connection_string = connection_string
        self.engine = create_engine(self.connection_string, future=True)
        self.session_builder = SessionBuilder(self.engine)
        self.metadata = Metadata
        self.metadata.create_all(bind=self.engine)

    def _paginate_select(self, stmt: Any, pageable: Pageable) -> Any:
        pass

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

    def get_all_by_filterable(self, f: Filterable, p: Optional[Pageable] = None) -> List[T] | PagedResult[List[T]]:
        with self.session_builder.open() as session:
            stmt = select(self.entity)
            stmt = self._filter_select(stmt, f)
            if p:
                stmt = self._paginate_select(stmt, p)
            return session.execute(stmt).scalars().all()

    def create(self, model: T) -> T:
        with self.session_builder.open() as session:
            return session.execute(insert(self.entity).values(**model.as_dict())).scalars().first()

    def create_in_batch(self, _: Session, models: List[T]):
        return [self.create(m) for m in models]

    def update(self, model: T) -> T:
        with self.session_builder.open() as session:
            return session.query(T).filter(T.id == model.id).update(model.__dict__)

    def update_in_batch(self, _: Session, models: T):
        return [self.update(m) for m in models]

    def delete(self, model_id: int) -> None:
        with self.session_builder.open() as s:
            return s.query(T).filter(T.id == model_id).delete()

    def delete_in_batch(self, model_ids: List[int]):
        return [self.delete(m) for m in model_ids]
