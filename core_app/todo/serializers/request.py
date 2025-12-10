# core_app/todo/serializers/request.py
from rest_framework import serializers

class TodoCreateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True, required=False)
    completed = serializers.BooleanField(default=False)

class TodoUpdateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(allow_blank=True, required=False)
    completed = serializers.BooleanField(required=False)
