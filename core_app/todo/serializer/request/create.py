from rest_framework import serializers
from core_app.todo.dataclasses.request.create import TodoCreateRequest

class TodoCreateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True, required=False)
    completed = serializers.BooleanField(default=False)

    def create(self, validated_data) -> TodoCreateRequest:
        return TodoCreateRequest(**validated_data)
