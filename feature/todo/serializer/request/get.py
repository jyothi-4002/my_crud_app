
from rest_framework import serializers
from feature.todo.dataclasses.request.get import TodoGetRequest

class TodoGetRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)

    def create(self, validated_data) -> TodoGetRequest:
        return TodoGetRequest(**validated_data)








