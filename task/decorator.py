import json
from functools import wraps

from task.model import TASKS
from task.store import FileStore


def sync_file(filename, mode='r', encoding='utf-8'):

    def decorator(func):

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)

            with FileStore(filename, mode=mode, encoding=encoding) as f:
                json.dump(TASKS, f)
        return wrapper
    return decorator
