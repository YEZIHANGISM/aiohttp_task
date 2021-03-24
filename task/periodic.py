import datetime
from threading import Timer

from task.settings import DATETIME_FORMAT, LOG_URL
from task.store import FileStore
from task.tasks import Task


class PeriodicTimer(Timer):
    def __init__(self, *args, **kwargs):
        super(PeriodicTimer, self).__init__(*args, **kwargs)

    def run(self):
        while not self.finished.is_set():
            self.finished.wait(self.interval)
            self.function(*self.args, **self.kwargs)


def will_be_expire(task):
    # 判断当前任务是否符合即将过期的标准

    if task.has_remind or not task.finished_at:
        return False
    time = datetime.datetime.strptime(task.finished_at, DATETIME_FORMAT)
    now = datetime.datetime.now()
    diff = now - time
    if -1 > diff.days > 1:
        return False
    diff_m = (diff.seconds - abs(diff.days * 24 * 60 * 60)) / 60
    if 0 > diff_m >= -60:
        return True
    return False


def expire_task():
    tasks = Task.get_list()
    if not tasks:
        print("no tasks")
        return

    for task in tasks:
        if will_be_expire(task):
            print(f"expire id: {task.task_id}")
            task.update(has_remind=1)
            filename = LOG_URL
            with FileStore(filename, mode='a+', encoding='utf-8') as f:
                content = " - ".join([datetime.datetime.strftime(datetime.datetime.now(), DATETIME_FORMAT),
                                      task.user_id,
                                      task.task_id,
                                      task.type_id,
                                      task.create_at,
                                      task.finished_at])
                f.write(content + "\n")


def register_task():
    timer = PeriodicTimer(5, expire_task)
    timer.setDaemon = True
    print("timer task start")
    timer.start()

