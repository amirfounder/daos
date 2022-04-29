from datetime import datetime, timezone

from sqlalchemy import update, Column, Integer, DateTime, select, func, insert

from daos.abstracts.database.config import Base, MetaData, Session


class Model(Base):
    __abstract__ = True
    __tablename__: str

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(True), default=datetime.utcnow)
    updated_at = Column(DateTime(True), default=datetime.utcnow)

    def __init__(self, **kwargs):
        self.model = type(self)

        now = datetime.now(timezone.utc)
        self.created_at = now
        self.updated_at = now

        self.from_dict(kwargs)

    @classmethod
    def columns(cls):
        return [c for c in MetaData.tables.get(cls.__tablename__).columns]

    @classmethod
    def column_names(cls):
        return [c.name for c in cls.columns()]

    def as_dict(self):
        return {n: v for n in self.column_names() if (v := getattr(self, n, None))}

    def from_dict(self, params):
        names = self.column_names()
        for k, v in params.items():
            if k in names:
                setattr(self, k, v)

    def load(self, id: int = None):
        if id:
            self.id = id

        if not self.id:
            return

        with Session() as session:
            result = session.get(self.model, self.id)

        self.from_dict(result.as_dict())

    def flush(self):
        now = datetime.now(timezone.utc)
        self.updated_at = now

        if not self.id:
            self.created_at = now
            query = insert(self.model).values(self.as_dict())

        else:
            query = update(self.model).where(self.model.id == self.id).values(self.as_dict())

        with Session() as session:
            return session.execute(query)

    @classmethod
    def all(cls, **kwargs):
        query = select(cls)

        columns = {c.name: c for c in cls.columns()}

        for k, vs in kwargs.items():

            # Clean kwargs
            if isinstance(k, str):
                if k.lower() not in columns:
                    del kwargs[k]
                else:
                    k = columns[k]
            if isinstance(k, Column):
                if k not in columns.values():
                    del kwargs[k]

            # Enable or clauses
            if not isinstance(vs, list):
                vs = [vs]

            # Apply where query clause
            query = query.where(
                k.in_([
                    func.lower(v) if isinstance(v, str) else v
                    for v in vs
                ])
            )

        with Session() as session:
            return session.execute(query).scalars().all()
