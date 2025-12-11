from rest_framework import serializers
from core_app.todo.dataclasses.request.getall import TodoGetAllRequest

class TodoGetAllRequestSerializer(serializers.Serializer):
    page_num = serializers.IntegerField(required=False, default=1)
    limit = serializers.IntegerField(required=False, default=50)

    def create(self, validated_data) -> TodoGetAllRequest:
        return TodoGetAllRequest(**validated_data)
