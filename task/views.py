import json

from aiohttp import web

from task.tasks import Task


def response(code=True, msg="success", data=None):
    resp = {"code": 1 and code or 0, "message": msg, "data": data or dict()}
    return web.json_response(text=json.dumps(resp))


async def create_task(request):
    # 创建任务
    form = await request.post()
    task = Task(**form)
    task.save()
    return response(data=task.line)


async def retrieve_task(request):
    # 查看任务详情
    task_id = request.match_info.get('task_id', None)
    if not task_id:
        return response(code=False, msg="参数缺失")
    task = Task.get(task_id=task_id)
    return response(data=task.line)


async def update_task(request):
    # 修改任务
    task_id = request.match_info.get('task_id', None)
    if not task_id:
        return response(code=False, msg="参数缺失")
    form = await request.post()
    task = Task.get(task_id=task_id)
    task.update(**form)
    return response()


async def delete_task(request):
    # 删除任务
    task_id = request.match_info.get('task_id', None)
    if not task_id:
        return response(code=False, msg="参数缺失")
    task = Task.get(task_id=task_id)
    task.delete()
    return response()
