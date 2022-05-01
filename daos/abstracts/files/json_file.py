import json

from daos.abstracts.files.base import File


class JsonFile(File):
    suffix = '.json'

    @File.contents.setter
    def contents(self, value):
        if isinstance(value, dict):
            value = json.dumps(value)
        super().contents = value

    def dict(self):
        return json.loads(self.contents)
