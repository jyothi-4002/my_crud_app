from rest_framework import serializers
from feature.musician.dataclasses.request.get import MusicianGetDC


class MusicianGetRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def create(self, validated_data):
        return MusicianGetDC(id=validated_data["id"])
