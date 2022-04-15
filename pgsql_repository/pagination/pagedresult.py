from typing import TypeVar, Generic, List

from pgsql_repository.pagination.pageable import Pageable

T = TypeVar('T')


class PagedResult(Generic[T]):
    def __init__(self, pageable: Pageable, results: List[T], count: int):
        self.pageable = pageable
        self.count = results
        self.results = count
