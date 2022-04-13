from sqlalchemy.orm import registry

mapper_registry: registry = registry()
PGSQLEntity = mapper_registry.generate_base()
