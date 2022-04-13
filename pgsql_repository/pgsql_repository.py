from typing import Generic, TypeVar, List, Optional, Callable

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, Session

from pgsql_repository.pageable import Pageable
from pgsql_repository.pagedresult import PagedResult
from pgsql_repository.pgsql_filterable import PGSQLFilterable

T = TypeVar('T')


def session_wrapper(func: Callable):
    def wrapper(self: PGSQLRepository, *args, **kwargs):
        with self._open_session() as session:
            session.begin()
            try:
                return func(session, *args, **kwargs)
            except Exception:
                session.rollback()
                raise
            finally:
                session.commit()
                session.close()
    return wrapper


class PGSQLRepository(Generic[T]):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self._engine = create_engine(self.connection_string)
        self._session = sessionmaker(bind=self._engine)

    def _open_session(self):
        return self._session()

    @session_wrapper
    def get_by_id(self, session: Session) -> T:
        return session.query(T).get(id)

    @session_wrapper
    def get_all(self, session: Session, pageable: Optional[Pageable] = None) -> List[T]:
        return session.query(T).all()

    @session_wrapper
    def get_by_filterable(self, session: Session, filterable: PGSQLFilterable, pageable: Optional[Pageable] = None) \
            -> List[T] | PagedResult[List[T]]:
        return session.query(T).all()

    @session_wrapper
    def create(self, session: Session, model: T) -> T:
        session.query(T).add_entity(model)
        return model

    @session_wrapper
    def update(self, session: Session, model: T) -> T:
        return session.query(T).filter(T.id == model.id).update(model.__dict__)

    @session_wrapper
    def delete(self, session: Session, model_id: int) -> None:
        return session.query(T).filter(T.id == model_id).delete()
