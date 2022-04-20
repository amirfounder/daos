from playhouse.reflection import generate_models


class SchemaLoader:
    def __init__(self, database, model):
        self.database = database
        self.model = model

    def _get_table_columns(self):
        pass

    def _get_model_columns(self):
        pass

    def load(self):
        existing_models = generate_models(self.database)
        if (name := getattr(self.model, 'table_name')) and name not in existing_models:
            self.model.create_table()
            return

        model_columns = self._get_model_columns()
        table_columns = self._get_table_columns()

        pass