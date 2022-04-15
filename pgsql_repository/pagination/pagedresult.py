from typing import TypeVar, Generic

from pgsql_repository.pagination.pageable import Pageable

T = TypeVar('T')


class PagedResult(Generic[T]):
    def __init__(self, pageable: Pageable, results: T, count: int):
        self.pageable = pageable
        self.count = results
        self.results = count
