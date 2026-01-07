# feature/todo/serializer/request/update.py
from rest_framework import serializers
from drf_spectacular.utils import OpenApiParameter
from feature.todo.dataclasses.request.update import TodoUpdateRequest


class TodoUpdateRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    title = serializers.CharField(required=False)
    description = serializers.CharField(allow_blank=True, required=False)
    completed = serializers.BooleanField(required=False)

    def create(self, validated_data) -> TodoUpdateRequest:
        return TodoUpdateRequest(**validated_data)

    @staticmethod
    def get_parameters():
        return [
            OpenApiParameter(name="id", description="Todo ID", required=True, type=int, location=OpenApiParameter.QUERY)
        ]
