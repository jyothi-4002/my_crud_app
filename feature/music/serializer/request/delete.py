from rest_framework import serializers
from feature.music.dataclasses.request.delete import MusicDeleteRequest

class MusicDeleteRequestSerializer(serializers.Serializer):
    ids = serializers.ListField(child=serializers.IntegerField())

    def create(self, validated_data):
        return MusicDeleteRequest(**validated_data)
