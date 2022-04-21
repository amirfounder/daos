from daos.abstracts.document.csv.repository import BaseCsvDocRepository as Repository
from daos.abstracts.document.csv.model import CsvDocumentModel as Model


class RawHtmlDocumentFeaturesRepository(Repository[Model]):
    def __init__(self, path: str):
        super().__init__(Model, path)
