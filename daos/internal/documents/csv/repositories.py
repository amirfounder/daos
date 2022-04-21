from daos.abstracts.document.csv.repository import BaseCsvDocRepository as Repository
from daos.abstracts.document.csv.model import CsvDocumentModel as Model
from daos.internal.paths import Paths


class HtmlOnlyHtmlDocumentFeaturesRepository(Repository[Model]):
    def __init__(self):
        super().__init__(Model, Paths.html_only_features.value)
