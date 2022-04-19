from typing import Dict, Any, Type

from sqlalchemy import func

from daos.base.database.model.model import BaseDatabaseModel


class BaseFilterable:
    def __init__(self, model: Type[BaseDatabaseModel], params: Dict):
        self.model = model
        self.params = params

        self._clean_filters()

    def _clean_filters(self) -> None:
        columns = self.model.get_columns()
        for k, v in self.params.items():
            if k.lower() not in columns:
                del self.params[k]

    def apply(self, sql_query: Any) -> Any:
        for key, value in self.params.items():
            sql_query = sql_query.where(
                getattr(self.model, key) == (
                    func.lower(value) if
                    isinstance(value, str)
                    else value
                )
            )
        return sql_query
