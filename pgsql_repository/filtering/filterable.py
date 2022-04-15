from typing import Dict


class Filterable:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.k = v
        self.filters: Dict = kwargs
