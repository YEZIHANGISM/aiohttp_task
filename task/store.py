
class FileStore:

    def __init__(self, filename, mode='r', **kwargs):
        self.filename = filename
        self.mode = mode
        self.kwargs = kwargs

    def __enter__(self):
        self.file = open(self.filename, mode=self.mode, **self.kwargs)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
