from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .controller import create_todo, get_all_todos, get_todo_by_id, update_todo, delete_todo
from .serializers.request import TodoRequest

@csrf_exempt
def create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        todo_req = TodoRequest(**data)
        response = create_todo(todo_req)
        return JsonResponse(response.__dict__)

@csrf_exempt
def get_all(request):
    if request.method == "GET":
        todos = get_all_todos()
        return JsonResponse([t.__dict__ for t in todos], safe=False)

@csrf_exempt
def get(request, todo_id):
    if request.method == "GET":
        todo = get_todo_by_id(todo_id)
        return JsonResponse(todo.__dict__)

@csrf_exempt
def update(request, todo_id):
    if request.method == "PUT":
        data = json.loads(request.body)
        todo_req = TodoRequest(**data)
        todo = update_todo(todo_id, todo_req)
        return JsonResponse(todo.__dict__)

@csrf_exempt
def delete(request, todo_id):
    if request.method == "DELETE":
        return JsonResponse(delete_todo(todo_id))
