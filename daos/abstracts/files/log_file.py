from os.path import getsize
from daos.abstracts.files.base import File


class LogFile(File):
    suffix = '.log'
    max_file_size = 25 * 1000 * 1000

    @classmethod
    def log(cls, message: str):
        last_doc_path = cls._last_document_path()
        size = getsize(last_doc_path)
        instance = cls() if size >= cls.max_file_size else cls(path=last_doc_path)

        with open(instance.path, 'a') as f:
            f.write(message)
