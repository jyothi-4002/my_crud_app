# feature/todo/serializer/request/delete.py
from rest_framework import serializers
from drf_spectacular.utils import OpenApiParameter
from feature.todo.dataclasses.request.delete import TodoDeleteRequest


class TodoDeleteRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    ids = serializers.ListField(child=serializers.IntegerField(), required=False)

    def validate(self, attrs):
        if not attrs.get("id") and not attrs.get("ids"):
            raise serializers.ValidationError("id or ids required")
        return attrs

    def create(self, validated_data) -> TodoDeleteRequest:
        return TodoDeleteRequest(**validated_data)

    @staticmethod
    def get_parameters():
        return [
            OpenApiParameter(name="ids", description="Comma-separated Todo IDs", required=True, type=str, location=OpenApiParameter.QUERY)
        ]
