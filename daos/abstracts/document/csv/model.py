from csv import DictReader, DictWriter
from typing import Optional, Dict, List

from ..model import DocumentModel


class CsvDocumentModel(DocumentModel):
    suffix = '.csv'

    def __init__(self, path: Optional[str] = None):
        super().__init__(path)
        self.contents: List[Dict] = []
        self.field_names: List[str] = []

    def _load_field_names(self):
        self.field_names = list(set([key for obj in self.contents for key in obj.keys()]))
        return self.field_names

    def flush_contents(self):
        with open(self.path, self.write_mode, encoding=self.encoding, newline='') as file:
            writer = DictWriter(file, self.field_names)
            writer.writeheader()
            writer.writerows(self.contents)

    def load_contents(self):
        with open(self.path, self.read_mode, encoding=self.encoding, newline='') as file:
            reader = DictReader(file)
            self.contents = [row for row in reader]

        return self.contents
