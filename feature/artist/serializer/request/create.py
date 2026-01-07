from rest_framework import serializers
from drf_spectacular.utils import OpenApiParameter
from feature.artist.dataclasses.request.create import ArtistCreateRequest


class ArtistCreateRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    description = serializers.CharField(required=False, allow_blank=True)
    debut_date = serializers.DateField(required=False)

    def create(self, validated_data):
        return ArtistCreateRequest(**validated_data)

    @staticmethod
    def get_parameters():
        """Swagger metadata for create operation"""
        return [
            OpenApiParameter(
                name="name",
                description="Artist name",
                required=True,
                type=str,
                location=OpenApiParameter.QUERY
            ),
            OpenApiParameter(
                name="age",
                description="Artist age",
                required=True,
                type=int,
                location=OpenApiParameter.QUERY
            ),
            OpenApiParameter(
                name="description",
                description="Artist description",
                required=False,
                type=str,
                location=OpenApiParameter.QUERY
            ),
            OpenApiParameter(
                name="debut_date",
                description="Debut date (YYYY-MM-DD)",
                required=False,
                type=str,
                location=OpenApiParameter.QUERY
            ),
        ]
