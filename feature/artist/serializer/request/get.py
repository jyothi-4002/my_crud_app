from rest_framework import serializers
from drf_spectacular.utils import OpenApiParameter
from feature.artist.dataclasses.request.get import ArtistGetRequest


class ArtistGetRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def create(self, validated_data):
        return ArtistGetRequest(**validated_data)

    @staticmethod
    def get_parameters():
        return [
            OpenApiParameter(
                name="id",
                description="Artist ID",
                required=True,
                type=int,
                location=OpenApiParameter.QUERY
            )
        ]
