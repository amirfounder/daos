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

    def load(self, _id: int = None):
        if _id:
            self.id = _id

        if not self.id:
            return

        with Session() as session:
            result = session.get(type(self), self.id)

        self.from_dict(result.as_dict())

    def flush(self):
        now = datetime.now(timezone.utc)
        self.updated_at = now

        if not self.id:
            self.created_at = now
            query = insert(type(self)).values(self.as_dict())

        else:
            query = update(type(self)).where(type(self).id == self.id).values(self.as_dict())

        with Session() as session:
            return session.execute(query)

    @classmethod
    def distinct(cls, column: str | Column):
        columns = {c.name: c for c in cls.columns()}

        if isinstance(column, str) and column in columns:
            column = columns[column]

        query = select(column).distinct()

        with Session() as session:
            return session.execute(query).scalars().all()

    @classmethod
    def get_or_create(cls, return_list_if_one: bool = False, **kwargs):
        if not (result := cls.all(**kwargs)):
            instance = cls(**kwargs)
            instance.flush()
            return [instance] if return_list_if_one else instance
        else:
            if not return_list_if_one and len(result) == 1:
                return result[0]
            return result

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

    def delete(self):
        with Session() as session:
            session.delete(self)
