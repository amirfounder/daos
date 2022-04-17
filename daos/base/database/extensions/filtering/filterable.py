from typing import Dict, Any

from sqlalchemy import func

from daos.base.database.model.model import BaseDBDaoModel


class BaseFilterable:
    def __init__(self, model: BaseDBDaoModel, filters: Dict[str, Any]):
        self.model = model
        self.filters = filters

        self._clean_filters()

    def _clean_filters(self) -> None:
        columns = self.model.get_columns()
        for k, v in self.filters.items():
            if k.lower() not in columns:
                del self.filters[k]

    def apply(self, sql_query: Any) -> Any:
        for key, value in self.filters.items():
            sql_query = sql_query.where(
                getattr(self.model, key) == (
                    func.lower(value) if
                    isinstance(value, str)
                    else value
                )
            )
        return sql_query
