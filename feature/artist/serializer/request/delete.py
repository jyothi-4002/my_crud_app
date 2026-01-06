from rest_framework import serializers
from feature.artist.dataclasses.request.delete import ArtistDeleteRequest


class ArtistDeleteRequestSerializer(serializers.Serializer):
    ids = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False
    )

    def create(self, validated_data):
        return ArtistDeleteRequest(**validated_data)
