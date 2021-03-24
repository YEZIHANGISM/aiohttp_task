import json
import threading
import uuid

from task.decorator import sync_file
from task.model import TASKS
from task.settings import STORE_FILE_NAME
from task.store import FileStore


class Task:

    """Task类"""

    def __init__(self, task_id=None, user_id=None, type_id=None, create_at=None, finished_at=None, content=None, has_remind=None):
        self.task_id = task_id
        self.user_id = user_id
        self.type_id = type_id
        self.create_at = create_at
        self.finished_at = finished_at
        self.content = content
        self.has_remind = has_remind

    @property
    def line(self):
        return {"task_id": self.task_id or "",
                "user_id": self.user_id or "",
                "type_id": self.type_id or "",
                "create_at": self.create_at or "",
                "finished_at": self.finished_at or "",
                "content": self.content or "",
                "has_remind": self.has_remind or 0}

    def __repr__(self):
        return f'Task<{json.dumps(self.line)}>'

    def __str__(self):
        return f'Task<{json.dumps(self.line)}>'

    def __getattr__(self, item):
        return item

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    @staticmethod
    def get_list():
        return [Task(**v) for k, v in TASKS.items()]

    @classmethod
    def get(cls, task_id=""):
        task = TASKS.get(task_id, None)
        if not task:
            return None
        return Task(**task)

    @sync_file(STORE_FILE_NAME, mode='w')
    def save(self):
        task_id = uuid.uuid4().hex
        self.task_id = task_id
        TASKS[task_id] = self.line

    @sync_file(STORE_FILE_NAME, mode='w')
    def update(self, **kwargs):
        TASKS[self.task_id].update(kwargs)

    @sync_file(STORE_FILE_NAME, mode='w')
    def delete(self):
        del TASKS[self.task_id]


def _load():
    # 加载文件
    global TASKS
    with FileStore(STORE_FILE_NAME, 'a+', encoding='utf-8') as f:
        f.seek(0)
        data = f.read()
        if not data:
            return
        TASKS = json.loads(data)


def load_data():
    t = threading.Thread(target=_load)
    t.start()
    t.join()
