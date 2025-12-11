
from rest_framework import serializers
from core_app.todo.dataclasses.request.get import TodoGetRequest

class TodoGetRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)

    def create(self, validated_data) -> TodoGetRequest:
        return TodoGetRequest(**validated_data)
