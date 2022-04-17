from __future__ import annotations


from daos.base.database.dao.sessions.session_context import SessionContext


class SessionBuilder:
    def __init__(self, engine):
        self.engine = engine

    def open(self) -> SessionContext:
        return SessionContext(self.engine)
