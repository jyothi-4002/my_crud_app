# core_app/todo/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from core_app.todo.serializers.request import (
    TodoCreateRequestSerializer, TodoUpdateRequestSerializer
)
from core_app.todo.serializers.response import TodoResponseSerializer
from core_app.todo.dataclasses.request import TodoRequest
from core_app.todo.controller import (
    create_todo, get_all_todos, get_todo_by_id, update_todo, delete_todo
)

@api_view(['POST'])
def create(request):
    serializer = TodoCreateRequestSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    validated = serializer.validated_data
    # create dataclass from validated data
    todo_req = TodoRequest(
        title=validated.get('title'),
        description=validated.get('description', ''),
        completed=validated.get('completed', False)
    )
    todo_resp = create_todo(todo_req)
    out = TodoResponseSerializer(todo_resp.__dict__).data
    return Response(out, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_all(request):
    todos = get_all_todos()
    out = [TodoResponseSerializer(t.__dict__).data for t in todos]
    return Response(out)

@api_view(['GET'])
def get(request, todo_id: int):
    todo = get_todo_by_id(todo_id)
    if todo is None:
        return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response(TodoResponseSerializer(todo.__dict__).data)

@api_view(['PUT', 'PATCH'])
def update(request, todo_id: int):
    # allow partial update for PATCH
    is_patch = request.method == 'PATCH'
    serializer = TodoUpdateRequestSerializer(data=request.data, partial=is_patch)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    validated = serializer.validated_data

    # Fetch existing todo for partial fields if needed
    current = get_todo_by_id(todo_id)
    if current is None:
        return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    # build a TodoRequest dataclass using existing values when missing (for PUT require full)
    title = validated.get('title') if 'title' in validated else current.title
    description = validated.get('description') if 'description' in validated else current.description
    completed = validated.get('completed') if 'completed' in validated else current.completed

    todo_req = TodoRequest(title=title, description=description, completed=completed)
    updated = update_todo(todo_id, todo_req)
    if updated is None:
        return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response(TodoResponseSerializer(updated.__dict__).data)

@api_view(['DELETE'])
def delete(request, todo_id: int):
    ok = delete_todo(todo_id)
    if not ok:
        return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'message': 'Todo deleted successfully'}, status=status.HTTP_200_OK)
