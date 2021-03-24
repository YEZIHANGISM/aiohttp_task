## 安装依赖库
```
pip install -r requirements.txt
```

## 运行程序
使用pycharm运行`/task/main.py`

## 接口说明

### 创建任务
```
- url: http://localhost:8080/task/
- method: POST
- body: {
    "type_id": "testtypeid",
    "user_id": "testuserid",
    "create_at": "2020-09-12 23:21:54",
    "finished_at": "2020-09-12 23:21:54",
    "content": "test content"
}
- response: {
    "code": true,
    "message": "success",
    "data": {
        "task_id": "c8d0020caa734013a2a0e85ee07071a9",
        "user_id": "yzh1",
        "type_id": "dfsfdsfds",
        "create_at": "2020-09-12 23:21:54",
        "finished_at": "2021-03-25 00:00:54",
        "content": "post2",
        "has_remind": 0
    }
}
```

### 修改任务
```
- url: http://localhost:8080/task/{task_id}
- method: PUT
- body: {
    "type_id": "testtypeid",
    "user_id": "testuserid",
    "create_at": "2020-09-12 23:21:54",
    "finished_at": "2020-09-12 23:21:54",
    "content": "test content"
}
- response: {
    "code": true,
    "message": "success",
    "data": {}
}
```

### 查看任务详情
```
- url: http://localhost:8080/task/{task_id}
- method: GET
- body: {}
- response: {
    "code": true,
    "message": "success",
    "data": {
        "task_id": "c8d0020caa734013a2a0e85ee07071a9",
        "user_id": "yzh1",
        "type_id": "dfsfdsfds",
        "create_at": "2020-09-12 23:21:54",
        "finished_at": "2021-03-25 00:00:54",
        "content": "post2",
        "has_remind": 0
    }
}
```

### 删除任务
```
- url: http://localhost:8080/task/{task_id}
- method: DELETE
- body: {}
- response: {
    "code": true,
    "message": "success",
    "data": {}
}
```