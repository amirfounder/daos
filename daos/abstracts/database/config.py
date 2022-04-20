from sqlalchemy.orm import registry, DeclarativeMeta
from sqlalchemy import MetaData, create_engine

POSTGRESQL_CONNECTION_STRING = 'postgresql://postgres:root@localhost:5432/postgres'

mapper_registry: registry = registry()
Base: DeclarativeMeta = mapper_registry.generate_base()
MetaData: MetaData = Base.metadata
engine = create_engine(POSTGRESQL_CONNECTION_STRING, future=True)
