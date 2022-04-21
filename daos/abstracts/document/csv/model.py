from csv import DictReader, DictWriter
from typing import Optional, Dict, List

from ..model import DocumentModel


class CsvDocumentModel(DocumentModel):
    suffix = '.csv'

    def __init__(self, path: Optional[str] = None):
        super().__init__(path)
        self.records: List[Dict] = []
        self.field_names: List[str] = []

    def _load_field_names(self):
        self.field_names = list(set([key for obj in self.records for key in obj.keys()]))
        return self.field_names

    def _flush_records(self):
        with open(self.path, self.write_mode, newline='') as file:
            writer = DictWriter(file, self.field_names)
            writer.writeheader()
            writer.writerows(self.records)

    def _load_records(self):
        with open(self.path, self.read_mode, newline='') as file:
            reader = DictReader(file)
            self.records = [row for row in reader]

        return self.records
