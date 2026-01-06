from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg import openapi
from common.swagger import SwaggerUtils
from feature.todo.views import TodoView
from feature.todo.utils import TodoUtils

from feature.todo.serializer.request.create import TodoCreateRequestSerializer
from feature.todo.serializer.request.get import TodoGetRequestSerializer
from feature.todo.serializer.request.getall import TodoGetAllRequestSerializer
from feature.todo.serializer.request.update import TodoUpdateRequestSerializer
from feature.todo.serializer.request.delete import TodoDeleteRequestSerializer

todo_view = TodoView()

@SwaggerUtils.create_endpoint(TodoCreateRequestSerializer, description="Create a new music record")
@api_view(["POST"])
def create_todo(request):
    serializer = TodoCreateRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    params = serializer.validated_data   # ✅ FIX HERE
    return todo_view.create(params)

@SwaggerUtils.get_endpoint(
    query_params=[{"name": "id", "type": "integer", "required": True, "description": "Music ID"}],
    description="Get music by ID"
)
@api_view(["GET"])
def get_todo(request):
    params = TodoUtils.get_query_params(request)
    serializer = TodoGetRequestSerializer(data=params)
    serializer.is_valid(raise_exception=True)

    return todo_view.get(serializer.validated_data)

@SwaggerUtils.get_endpoint(
    query_params=[{"name": "page_num", "type": "integer", "required": False, "description": "Page number"}],
    description="Get all music records"
)
@api_view(["GET"])
def get_all_todos(request):
    params = TodoUtils.get_query_params(request)
    serializer = TodoGetAllRequestSerializer(data=params)
    serializer.is_valid(raise_exception=True)

    return todo_view.get_all(serializer.validated_data, request)

@SwaggerUtils.update_endpoint(
    TodoUpdateRequestSerializer,
    query_params=[{"name": "id", "type": "integer", "required": True, "description": "Music ID"}],
    description="Update music by ID"
)
@api_view(["PUT", "PATCH"])
def update_todo(request):
    params = TodoUtils.get_query_params(request)

    if "id" not in params:
        return Response(
            TodoUtils.error_response_data("Todo id is required", "id missing"),
            status=400
            )

    data = request.data.copy()
    data["id"] = int(params["id"])  # ✅ inject id into body

    serializer = TodoUpdateRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)


    return todo_view.update(serializer.validated_data)

@SwaggerUtils.delete_endpoint(
    query_params=[{"name": "ids", "type": "string", "required": True, "description": "Comma-separated music IDs"}],
    description="Delete music(s)"
)
@api_view(["DELETE"])
def delete_todo(request):
    params = TodoUtils.get_query_params(request)

    serializer = TodoDeleteRequestSerializer(data=params)
    serializer.is_valid(raise_exception=True)

    # ✅ CALL EXISTING METHOD
    return todo_view.delete(serializer.validated_data)