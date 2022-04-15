from enum import Enum


class SortDirection(Enum):
    ASC = 'asc'
    DESC = 'desc'


class Sortable:
    def __init__(self, column: str, direction: SortDirection = SortDirection.ASC):
        self.column = column
        self.direction = direction
