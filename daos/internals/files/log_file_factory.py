from daos.abstracts.files.log_file import LogFile


class LogFileFactory:
    @staticmethod
    def get_log_file(dir_name: str):
        class _LogFile(LogFile):
            dir_path = 'C:/ml-studies/logs/' + dir_name.removeprefix('/')
        return _LogFile
