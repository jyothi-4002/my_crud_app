from rest_framework import serializers
from feature.music.dataclasses.request.get import MusicGetRequest

class MusicGetRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def create(self, validated_data):
        return MusicGetRequest(**validated_data)
