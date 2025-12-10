# core_app/todo/serializers/response.py
from rest_framework import serializers

class TodoResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField(allow_blank=True)
    completed = serializers.BooleanField()
    created_at = serializers.CharField()
    updated_at = serializers.CharField()
