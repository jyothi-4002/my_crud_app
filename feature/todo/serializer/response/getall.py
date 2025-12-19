from rest_framework import serializers
from feature.todo.dataclasses.response.getall import TodoGetAllResponse, TodoGetAllItem

class TodoGetAllItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField(allow_blank=True)
    completed = serializers.BooleanField()
    created_at = serializers.CharField()
    updated_at = serializers.CharField()

    def create(self, validated_data) -> TodoGetAllItem:
        return TodoGetAllItem(**validated_data)

class TodoGetAllResponseSerializer(serializers.Serializer):
    results = TodoGetAllItemSerializer(many=True)
    page_num = serializers.IntegerField()
    total_page = serializers.IntegerField()
    total_count = serializers.IntegerField()
    next_page_required = serializers.BooleanField()

    def create(self, validated_data) -> TodoGetAllResponse:
        validated_data["results"] = [
            TodoGetAllItem(**item) for item in validated_data.get("results", [])
        ]
        return TodoGetAllResponse(**validated_data)
