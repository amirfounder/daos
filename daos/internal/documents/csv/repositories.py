from daos.abstracts.document.csv.repository import BaseCsvDocRepository as Repository
from daos.abstracts.document.csv.model import CsvDocumentModel as Model
from daos.internal.paths import Paths


class ProcessedHtmlV1DocumentFeaturesRepository(Repository[Model]):
    def __init__(self):
        super().__init__(Model, Paths.processed_html_v1_features.value)
