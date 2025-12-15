from rest_framework import serializers
from core_app.feature.todo.dataclasses.response.delete import TodoDeleteResponse

class TodoDeleteResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)


    def create(self, validated_data) -> TodoDeleteResponse:
        return TodoDeleteResponse(**validated_data)
