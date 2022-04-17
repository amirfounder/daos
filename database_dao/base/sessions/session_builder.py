from __future__ import annotations


from database_dao.base.sessions.session_context import SessionContext


class SessionBuilder:
    def __init__(self, engine):
        self.engine = engine

    def open(self) -> SessionContext:
        return SessionContext(self.engine)
