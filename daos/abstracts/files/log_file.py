import warnings

from daos.abstracts.files.base import File


class LogFile(File):
    suffix = '.log'

    def __init__(self):
        super().__init__(path=self.last_file_path)

    def log(self, message: str):
        if self.exceeds_max_file_size:
            warnings.warn(f"Max file size exceeded for log file: {self.dir_path}")

        self.load()
        self.contents += message + '\n'
        self.flush()
