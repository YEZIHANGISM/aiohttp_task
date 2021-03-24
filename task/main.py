from aiohttp import web

from task.routes import setup_routes
from task.tasks import load_data
from task.periodic import register_task


if __name__ == '__main__':
    app = web.Application()
    setup_routes(app)

    # 加载文件数据至内存
    load_data()

    # 定时任务
    register_task()
    web.run_app(app)
