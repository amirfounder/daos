from sqlalchemy.orm import registry, DeclarativeMeta, Session as SqlAlchemySession
from sqlalchemy import MetaData, create_engine


POSTGRESQL_CONNECTION_STRING = 'postgresql://postgres:root@localhost:5432/postgres'

mapper_registry: registry = registry()
Base: DeclarativeMeta = mapper_registry.generate_base()
MetaData: MetaData = Base.metadata
engine = create_engine(POSTGRESQL_CONNECTION_STRING, future=True)

class Session:
    def __init__(self):
        self.session: SqlAlchemySession

    def __enter__(self):
        self.session = SqlAlchemySession(bind=engine)
        self.session.begin()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.session.rollback()
            return False

        self.session.expunge_all()
        self.session.commit()
        self.session.close()
