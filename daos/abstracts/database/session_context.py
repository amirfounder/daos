from sqlalchemy.orm import Session
from .config import engine


class SessionContext:
    def __init__(self):
        self.session: Session

    def __enter__(self):
        self.session = Session(bind=engine)
        self.session.begin()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.session.rollback()
            return False

        self.session.expunge_all()
        self.session.commit()
        self.session.close()

