from rest_framework import serializers
from core_app.todo.dataclasses.request.update import TodoUpdateRequest

class TodoUpdateRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    title = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(allow_blank=True, required=False)
    completed = serializers.BooleanField(required=False)

    def create(self, validated_data) -> TodoUpdateRequest:
        return TodoUpdateRequest(**validated_data)
