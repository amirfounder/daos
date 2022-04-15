from __future__ import annotations
from typing import Generic, TypeVar, List, Optional, Callable

from sqlalchemy import select, insert, func
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session

from pgsql_repository.core import Metadata
from pgsql_repository.pageable import Pageable
from pgsql_repository.pagedresult import PagedResult
from pgsql_repository.filterable import Filterable
from pgsql_repository.entity import Base as Entity

T = TypeVar('T')


def session_wrapper(_func: Callable):
    def wrapper(self: Repository, *args, **kwargs):
        if not isinstance(self, Repository):
            raise Exception('@session_wrapper must be called on a PGSQLRepository method.')
        with self._open_session() as session:
            session.begin()
            try:
                return _func(self, session, *args, **kwargs)
            except Exception:
                session.rollback()
                raise
            finally:
                session.commit()
                session.close()

    return wrapper


class Repository(Generic[T]):
    def __init__(self, entity: Entity, connection_string: str):
        self.connection_string = connection_string
        self.entity = entity
        self.engine = create_engine(self.connection_string, future=True)
        self._emit_table_ddl()

    def _emit_table_ddl(self):
        Metadata.create_all(bind=self.engine)

    def _open_session(self):
        return Session(self.engine)

    @session_wrapper
    def get_by_id(self, session: Session, _id: int) -> T:
        session.get(self.entity, _id)

    def _get_all_by_pageable(self, session: Session, pageable: Pageable):
        pass

    @session_wrapper
    def get_all(self, session: Session, pageable: Optional[Pageable] = None) -> List[T]:
        if pageable:
            return self._get_all_by_pageable(session, pageable)
        return session.execute(select(self.entity)).scalars().all()

    @session_wrapper
    def get_by_filterable(self, session: Session, filterable: Filterable, pageable: Optional[Pageable] = None) \
            -> List[T] | PagedResult[List[T]]:
        stmt = select(self.entity)
        for k, v in filterable.filters.items():
            stmt = stmt.where(getattr(self.entity, k) == func.lower(v) if isinstance(v, str) else v)

        return session.execute(stmt).scalars().all()

    @session_wrapper
    def create(self, session: Session, model: T) -> T:
        return session.execute(insert(self.entity).values(**model.as_dict())).scalars().first()

    @session_wrapper
    def create_in_batch(self, _: Session, models: List[T]):
        # TODO Update this for performance.
        return [self.create(m) for m in models]

    @session_wrapper
    def update(self, session: Session, model: T) -> T:
        return session.query(T).filter(T.id == model.id).update(model.__dict__)

    @session_wrapper
    def update_in_batch(self, _: Session, models: T):
        # TODO Update this for performance.
        return [self.update(m) for m in models]

    @session_wrapper
    def delete(self, session: Session, model_id: int) -> None:
        return session.query(T).filter(T.id == model_id).delete()
