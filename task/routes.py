from task.views import create_task, retrieve_task, update_task, delete_task


def setup_routes(app):
    app.router.add_post('/task/', create_task)
    app.router.add_get('/task/{task_id}', retrieve_task)
    app.router.add_put('/task/{task_id}', update_task)
    app.router.add_delete('/task/{task_id}', delete_task)
