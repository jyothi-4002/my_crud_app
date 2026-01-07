from rest_framework import serializers
from drf_spectacular.utils import OpenApiParameter
from feature.artist.dataclasses.request.delete import ArtistDeleteRequest


class ArtistDeleteRequestSerializer(serializers.Serializer):
    ids = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False
    )

    def create(self, validated_data):
        return ArtistDeleteRequest(**validated_data)

    @staticmethod
    def get_parameters():
        return [
            OpenApiParameter(
                name="ids",
                description="Comma separated artist IDs",
                required=True,
                type=str,
                location=OpenApiParameter.QUERY
            )
        ]
