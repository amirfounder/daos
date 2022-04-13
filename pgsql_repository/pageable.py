from enum import Enum


class SortDirection(Enum):
    ASC = 'asc'
    DESC = 'desc'


class Sortable:
    def __init__(self, column: str, direction: SortDirection = SortDirection.ASC):
        self.column = column
        self.direction = direction


class Pageable:
    def __init__(self, page: int, count: int, sorting: Sortable):
        self.page = page
        self.count = count
        self.sorting = sorting

