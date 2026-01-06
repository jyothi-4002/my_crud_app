from rest_framework import serializers
from feature.artist.dataclasses.request.getall import ArtistGetAllRequest

class ArtistGetAllRequestSerializer(serializers.Serializer):
    page_num = serializers.IntegerField(required=False, default=1)
    limit = serializers.IntegerField(required=False, default=10)

    def create(self, validated_data):
        return ArtistGetAllRequest(**validated_data)
