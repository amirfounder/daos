from sqlalchemy.orm import registry, DeclarativeMeta
from sqlalchemy import MetaData

mapper_registry: registry = registry()
Base: DeclarativeMeta = mapper_registry.generate_base()
Metadata: MetaData = Base.metadata
