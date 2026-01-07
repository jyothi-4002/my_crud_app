# feature/todo/serializer/request/create.py
from rest_framework import serializers
from drf_spectacular.utils import OpenApiParameter
from feature.todo.dataclasses.request.create import TodoCreateRequest


class TodoCreateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=False, required=False)
    completed = serializers.BooleanField(default=False)

    def create(self, validated_data) -> TodoCreateRequest:
        return TodoCreateRequest(**validated_data)

    @staticmethod
    def get_parameters():
        return [
            OpenApiParameter(name="title", description="Todo title", required=True, type=str, location=OpenApiParameter.QUERY),
            OpenApiParameter(name="description", description="Todo description", required=False, type=str, location=OpenApiParameter.QUERY),
            OpenApiParameter(name="completed", description="Completion status", required=False, type=bool, location=OpenApiParameter.QUERY),
        ]
