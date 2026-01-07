# feature/todo/controller.py
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from feature.todo.views import TodoView
from feature.todo.utils import TodoUtils

from feature.todo.serializer.request.create import TodoCreateRequestSerializer
from feature.todo.serializer.request.get import TodoGetRequestSerializer
from feature.todo.serializer.request.getall import TodoGetAllRequestSerializer
from feature.todo.serializer.request.update import TodoUpdateRequestSerializer
from feature.todo.serializer.request.delete import TodoDeleteRequestSerializer


class TodoController:

    @staticmethod
    @extend_schema(
        description="Create a new Todo",
        request=TodoCreateRequestSerializer,
        parameters=TodoCreateRequestSerializer.get_parameters()
    )
    @api_view(["POST"])
    def create(request: Request) -> Response:
        serializer = TodoCreateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return TodoView().create(serializer.save())

    @staticmethod
    @extend_schema(
        description="Get a Todo by ID",
        parameters=TodoGetRequestSerializer.get_parameters()
    )
    @api_view(["GET"])
    def get(request: Request) -> Response:
        params = TodoUtils.get_query_params(request)
        serializer = TodoGetRequestSerializer(data=params)
        serializer.is_valid(raise_exception=True)
        return TodoView().get(serializer.save())

    @staticmethod
    @extend_schema(
        description="Get all Todos",
        parameters=TodoGetAllRequestSerializer.get_all_parameters()
    )
    @api_view(["GET"])
    def get_all(request: Request) -> Response:
        params = TodoUtils.get_query_params(request)
        serializer = TodoGetAllRequestSerializer(data=params)
        serializer.is_valid(raise_exception=True)
        return TodoView().get_all(serializer.save(), request)

    @staticmethod
    @extend_schema(
        description="Update a Todo",
        request=TodoUpdateRequestSerializer,
        parameters=TodoUpdateRequestSerializer.get_parameters()
    )
    @api_view(["PUT", "PATCH"])
    def update(request: Request) -> Response:
        params = TodoUtils.get_query_params(request)
        data = request.data.copy()
        data["id"] = int(params["id"])
        serializer = TodoUpdateRequestSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return TodoView().update(serializer.save())

    @staticmethod
    @extend_schema(
        description="Delete Todo(s)",
        parameters=TodoDeleteRequestSerializer.get_parameters()
    )
    @api_view(["DELETE"])
    def delete(request: Request) -> Response:
        params = TodoUtils.get_query_params(request)
        serializer = TodoDeleteRequestSerializer(data=params)
        serializer.is_valid(raise_exception=True)
        return TodoView().delete(serializer.save())
