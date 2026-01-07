# feature/todo/serializer/request/getall.py
from rest_framework import serializers
from drf_spectacular.utils import OpenApiParameter
from feature.todo.dataclasses.request.getall import TodoGetAllRequest


class TodoGetAllRequestSerializer(serializers.Serializer):
    page_num = serializers.IntegerField(required=False, default=1, min_value=1)
    limit = serializers.IntegerField(required=False, default=10, min_value=1, max_value=100)

    def create(self, validated_data) -> TodoGetAllRequest:
        return TodoGetAllRequest(**validated_data)

    @staticmethod
    def get_all_parameters():
        return [
            OpenApiParameter(name="page_num", description="Page number", required=False, type=int, location=OpenApiParameter.QUERY),
            OpenApiParameter(name="limit", description="Items per page", required=False, type=int, location=OpenApiParameter.QUERY)
        ]
