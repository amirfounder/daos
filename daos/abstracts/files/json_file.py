import json

from daos.abstracts.files.base import File


class JsonFile(File):
    suffix = '.html'

    def dict(self):
        return json.loads(self.contents)
