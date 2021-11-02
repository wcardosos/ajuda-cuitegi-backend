class FileStub:
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def readlines(self):
        return [
            'from src.packages.Class import Class\n',
            'from src.packages.OtherClass import OtherClass\n',
            '\n',
            'n = 1'
        ]