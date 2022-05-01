from daos.abstracts.files.base import File


class LogFile(File):
    suffix = '.log'

    def __init__(self, path: str = None):
        if not path:
            path = self.last_file_path
        super().__init__(path=path)

    @classmethod
    def log(cls, message: str):
        instance = cls()
        if instance.exceeds_max_file_size:
            # noinspection PyTypeChecker
            instance = cls(path=cls.next_file_path)

        instance.load()
        instance.contents += message + '\n'
        instance.flush()
