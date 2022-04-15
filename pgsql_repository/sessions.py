from __future__ import annotations
from sqlalchemy.orm import Session


class SessionBuilder:
    def __init__(self, engine):
        self.engine = engine

    def open(self) -> SessionContext:
        return SessionContext(self.engine)


class SessionContext:
    def __init__(self, engine):
        self.engine = engine
        self.session: Session

    def __enter__(self):
        self.session = Session(binds=self.engine)
        self.session.begin()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.session.rollback()
        self.session.commit()
        self.session.close()
