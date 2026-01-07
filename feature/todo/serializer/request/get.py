# feature/todo/serializer/request/get.py
from rest_framework import serializers
from drf_spectacular.utils import OpenApiParameter
from feature.todo.dataclasses.request.get import TodoGetRequest


class TodoGetRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)

    def create(self, validated_data) -> TodoGetRequest:
        return TodoGetRequest(**validated_data)

    @staticmethod
    def get_parameters():
        return [
            OpenApiParameter(name="id", description="Todo ID", required=True, type=int, location=OpenApiParameter.QUERY)
        ]
