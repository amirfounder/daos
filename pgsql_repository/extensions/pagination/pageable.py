from pgsql_repository.extensions.pagination.sortable import Sortable, SortDirection


class Pageable:
    def __init__(self, page: int = 1, size: int = 25, sorting: Sortable = Sortable('id', SortDirection.ASC)):
        self.page = page
        self.size = size
        self.sorting = sorting
