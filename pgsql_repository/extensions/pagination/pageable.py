from pgsql_repository.extensions.pagination.sortable import Sortable, SortDirection


class BasePageable:
    def __init__(self, page: int = 1, size: int = 25, sorting: Sortable = Sortable('id', SortDirection.ASC)):
        self.page = page
        self.size = size
        self.sorting = sorting
    
    def apply(self, sql_query):
        sql_query.offset(self.page * self.size).limit(self.size)
