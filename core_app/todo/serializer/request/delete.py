from rest_framework import serializers
from core_app.todo.dataclasses.request.delete import TodoDeleteRequest

class TodoDeleteRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    ids = serializers.ListField(child=serializers.IntegerField(), required=False)

    def validate(self, data):
        if not data.get("id") and not data.get("ids"):
            raise serializers.ValidationError("Either 'id' or 'ids' must be provided.")
        return data

    def create(self, validated_data) -> TodoDeleteRequest:
        return TodoDeleteRequest(**validated_data)
