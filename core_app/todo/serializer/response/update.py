from rest_framework import serializers
from core_app.todo.dataclasses.response.update import TodoUpdateResponse

class TodoUpdateResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField(allow_blank=True)
    completed = serializers.BooleanField()
    created_at = serializers.CharField()
    updated_at = serializers.CharField()

    def create(self, validated_data) -> TodoUpdateResponse:
        return TodoUpdateResponse(**validated_data)

