from daos.abstracts.database.repository import BaseDBRepository as Repository
from daos.internal.database.models import DocumentIndexModel as Model


class DocumentIndexRepository(Repository[Model]):
    def __init__(self): super().__init__(Model)
