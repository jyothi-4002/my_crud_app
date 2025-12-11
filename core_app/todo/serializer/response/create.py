from rest_framework import serializers
from core_app.todo.dataclasses.response.create import TodoCreateResponse

class TodoCreateResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField(allow_blank=True)
    completed = serializers.BooleanField()
    created_at = serializers.CharField()
    updated_at = serializers.CharField()

    def create(self, validated_data) -> TodoCreateResponse:
        return TodoCreateResponse(**validated_data)
