from rest_framework import serializers
from feature.artist.dataclasses.request.get import ArtistGetRequest

class ArtistGetRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def create(self, validated_data):
        return ArtistGetRequest(**validated_data)
