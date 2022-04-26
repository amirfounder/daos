from daos.abstracts.database.config import MetaData, engine, Session


TYPE_ALIASES = {
    'VARCHAR': 'CHARACTER VARYING',
    'INT8': 'BIGINT',
    'SERIAL8': 'BIGSERIAL',
    'VARBIT': 'BIT VARYING',
    'BOOL': 'BOOLEAN',
    'CHAR': 'CHARACTER',
    'FLOAT8': 'DOUBLE PRECISION',
    'INT': 'INTEGER',
    'INT4': 'INTEGER',
    'DECIMAL': 'NUMERIC',
    'FLOAT4': 'REAL',
    'INT2': 'SMALLINT',
    'SERIAL2': 'SMALLSERIAL',
    'SERIAL4': 'SERIAL',
    'TIMETZ': 'TIME WITH TIME ZONE',
    'TIMESTAMPTZ': 'TIMESTAMP WITH TIME ZONE',
}


def _select_pgsql_columns(table: str):
    with Session() as session:
        return session.execute(
            '''
            select column_name, data_type
            from information_schema.columns
            where table_name = '{table}'
            and table_schema = 'public'
            '''.format(table=table)
        ).all()


def _add_columns_to_pgsql(table: str, columns: list[list[str]]):
    add_column_statements = ', '.join([f'ADD COLUMN {n} {c}' for n, c in columns])
    alter_table_statement = f'ALTER TABLE {table} {add_column_statements}'
    with Session() as session:
        session.execute(alter_table_statement)


def setup_schema():
    MetaData.create_all(bind=engine)
    for table in MetaData.tables.values():
        columns = {c.name: c for c in table.columns}

        pgsql_columns = [[n, t.upper()] for n, t in _select_pgsql_columns(table.name)]
        model_columns = [[n, c.type.compile(dialect=engine.dialect)] for n, c in columns.items()]

        for i, (n, t) in enumerate(model_columns):
            if t in TYPE_ALIASES:
                model_columns[i][1] = TYPE_ALIASES[t]

        if columns_to_add := [c for c in model_columns if c not in pgsql_columns]:
            _add_columns_to_pgsql(table.name, columns_to_add)
