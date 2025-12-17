from rest_framework import serializers
from core_app.feature.music.dataclasses.request.update import MusicUpdateRequest

class MusicUpdateRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(required=False)
    singer = serializers.CharField(required=False)
    writer = serializers.CharField(required=False)
    description = serializers.CharField(required=False)

    def create(self, validated_data):
        return MusicUpdateRequest(**validated_data)
