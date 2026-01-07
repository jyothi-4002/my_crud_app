from rest_framework import serializers
from drf_spectacular.utils import OpenApiParameter
from feature.artist.dataclasses.request.update import ArtistUpdateRequest


class ArtistUpdateRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    description = serializers.CharField(required=False)
    debut_date = serializers.DateField(required=False)

    def create(self, validated_data):
        return ArtistUpdateRequest(**validated_data)

    @staticmethod
    def get_parameters():
        return [
            OpenApiParameter(
                name="id",
                description="Artist ID to update",
                required=True,
                type=int,
                location=OpenApiParameter.QUERY
            )
        ]
