from rest_framework import serializers
from feature.todo.dataclasses.request.getall import TodoGetAllRequest

class TodoGetAllRequestSerializer(serializers.Serializer):
    page_num = serializers.IntegerField(required=False, default=1,min_value=1)
    limit = serializers.IntegerField(required=False, default=10,min_value=1, max_value=100)

    def create(self, validated_data) -> TodoGetAllRequest:
        return TodoGetAllRequest(**validated_data)






