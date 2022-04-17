from typing import List, Type

from sqlalchemy import Column, MetaData
from sqlalchemy.engine import Engine

from database_dao.model import BaseModel
from database_dao.base.sessions import SessionBuilder


class SchemaLoader:
    def __init__(
            self,
            model: Type[BaseModel],
            metadata: MetaData,
            session_builder: SessionBuilder
    ):
        self.model = model
        self.metadata = metadata
        self.session_builder = session_builder

    def _get_pgsql_columns_by_table(self, table: str):
        with self.session_builder.open() as session:
            return session.execute(
                '''
                select column_name
                from information_schema.columns
                where table_name = '{table}'
                and table_schema = 'public'
                '''.format(table=table)
            ).scalars().all()

    def _remove_columns(self, table: str, columns: List[str]):
        drop_column_statements = ', '.join([f'DROP COLUMN {c}' for c in columns])
        alter_table_statement = f'ALTER TABLE {table} {drop_column_statements};'
        with self.session_builder.open() as session:
            session.execute(alter_table_statement)

    def _create_columns(self, table: str, columns: List[Column]):
        add_column_statements = ', '.join([f'ADD COLUMN {c.name} {c.type.compile()}' for c in columns])
        alter_table_statement = f'ALTER TABLE {table} {add_column_statements}'
        with self.session_builder.open() as session:
            session.execute(alter_table_statement)

    def load(self):
        for table in self.metadata.tables:
            model_columns_map = self.model.get_columns()
            model_columns = [k for k in model_columns_map]
            pgsql_columns = self._get_pgsql_columns_by_table(table)

            columns_to_remove = [c for c in pgsql_columns if c not in model_columns]
            columns_to_create = [model_columns_map.get(c) for c in model_columns if c not in pgsql_columns]

            if columns_to_create:
                self._create_columns(table, columns_to_create)
            if columns_to_remove:
                self._remove_columns(table, columns_to_remove)
