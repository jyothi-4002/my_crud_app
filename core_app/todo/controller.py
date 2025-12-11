# core_app/todo/controller.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core_app.todo.views import TodoView
from core_app.todo.dataclasses.request.create import TodoCreateRequest
from core_app.todo.dataclasses.request.update import TodoUpdateRequest
from core_app.todo.dataclasses.request.get import TodoGetRequest
from core_app.todo.dataclasses.request.getall import TodoGetAllRequest
from core_app.todo.dataclasses.request.delete import TodoDeleteRequest

todo_view = TodoView()


@api_view(['POST'])
def create_todo(request):
    params = TodoCreateRequest(**request.data)
    return todo_view.create_extract(params)


@api_view(['GET'])
def get_all_todos(request):
    params = TodoGetAllRequest(**request.query_params)
    return todo_view.get_all_extract(params)


@api_view(['GET'])
def get_todo(request, todo_id):
    params = TodoGetRequest(id=todo_id)
    return todo_view.get_extract(params)


@api_view(['PUT', 'PATCH'])
def update_todo(request, todo_id):
    params = TodoUpdateRequest(id=todo_id, **request.data)
    return todo_view.update_extract(params, todo_id=todo_id)


@api_view(['DELETE'])
def delete_todo(request, todo_id):
    params = TodoDeleteRequest(id=todo_id)
    return todo_view.delete_extract(params)
