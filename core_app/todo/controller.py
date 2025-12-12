# core_app/todo/controller.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core_app.todo.views import TodoView

# ⬇ import serializers (NOT dataclasses anymore)
from core_app.todo.serializer.request.create import TodoCreateRequestSerializer
from core_app.todo.serializer.request.getall import TodoGetAllRequestSerializer
from core_app.todo.serializer.request.get import TodoGetRequestSerializer
from core_app.todo.serializer.request.update import TodoUpdateRequestSerializer
from core_app.todo.serializer.request.delete import TodoDeleteRequestSerializer

todo_view = TodoView()


@api_view(['POST'])
def create_todo(request):
    serializer = TodoCreateRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    params = serializer.save()   # returns TodoCreateRequest dataclass
    return todo_view.create_extract(params)


@api_view(['GET'])
def get_all_todos(request):
    serializer = TodoGetAllRequestSerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)

    params = serializer.save()   # returns TodoGetAllRequest dataclass
    return todo_view.get_all_extract(params)


@api_view(['GET'])
def get_todo(request, todo_id):
    serializer = TodoGetRequestSerializer(data={"id": todo_id})
    serializer.is_valid(raise_exception=True)

    params = serializer.save()   # returns TodoGetRequest dataclass
    return todo_view.get_extract(params)


@api_view(['PUT', 'PATCH'])
def update_todo(request, todo_id):
    data = {"id": todo_id, **request.data}

    serializer = TodoUpdateRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    params = serializer.save()   # returns TodoUpdateRequest dataclass
    return todo_view.update_extract(params, todo_id=todo_id)


@api_view(['DELETE'])
def delete_todo(request, todo_id):
    serializer = TodoDeleteRequestSerializer(data={"id": todo_id})
    serializer.is_valid(raise_exception=True)

    params = serializer.save()   # returns TodoDeleteRequest dataclass
    return todo_view.delete_extract(params)
