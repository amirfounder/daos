from daos.abstracts.files.base import File


class LogFile(File):
    suffix = '.log'
    max_file_size = 25 * 1000 * 1000

    def log(self, message: str):
        if self.exceeds_max_size():
            raise Exception('Max file size reached.')

        with open(self.path, 'a') as f:
            f.write(message + '\n')

    def exceeds_max_size(self):
        return self.get_size() > self.max_file_size
