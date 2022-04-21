from daos import Paths
from daos.abstracts.document.csv.repository import BaseCsvDocRepository as Repository
from daos.abstracts.document.csv.model import CsvDocumentModel as Model


class HtmlOnlyHtmlDocumentFeaturesRepository(Repository[Model]):
    def __init__(self):
        super().__init__(Model, Paths.html_only_features.value)
