from enum import Enum


class SortDirection(Enum):
    ASC = 'asc'
    DESC = 'desc'


class Sortable:
    def __init__(self, column: str, direction: SortDirection = SortDirection.ASC):
        self.column = column
        self.direction = direction


class Pageable:
    def __init__(self, page: int = 1, size: int = 25, sorting: Sortable = Sortable('id', SortDirection.ASC)):
        self.page = page
        self.size = size
        self.sorting = sorting
