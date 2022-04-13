from sqlalchemy.orm import registry

mapper_registry: registry = registry()
PGSQLModel = mapper_registry.generate_base()
