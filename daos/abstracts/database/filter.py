from typing import Dict, Any, Type, TypeVar, Generic

from sqlalchemy import func, Column

T = TypeVar('T')


class BaseFilter(Generic[T]):
    def __init__(self, model: Type[T], params: Dict):
        self.model = model
        self.params = params

    def _clean_filters(self) -> None:
        columns = self.model.get_columns()
        for k, v in self.params.items():
            if isinstance(k, str):
                if k.lower() not in columns:
                    del self.params[k]
                else:
                    self.params[k] = columns[k]
            if isinstance(k, Column):
                if k not in columns.values():
                    del self.params[k]

    def apply(self, sql_query: Any) -> Any:
        self._clean_filters()
        for column, value in self.params.items():
            sql_query = sql_query.where(
                column == (
                    func.lower(value) if
                    isinstance(value, str)
                    else value
                )
            )
        return sql_query
