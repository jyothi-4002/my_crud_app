from rest_framework import serializers
from drf_spectacular.utils import OpenApiParameter
from feature.music.dataclasses.request.create import MusicCreateRequest


class MusicCreateRequestSerializer(serializers.Serializer):
    title = serializers.CharField()
    artist_id = serializers.IntegerField()
    singer = serializers.CharField()
    writer = serializers.CharField()
    description = serializers.CharField(required=False, allow_blank=True)
    released_date = serializers.DateField(required=False)

    def create(self, validated_data):
        return MusicCreateRequest(**validated_data)

    @staticmethod
    def get_parameters():
        """Swagger metadata for create operation"""
        return [
            OpenApiParameter(
                name="title",
                description="Title of the music",
                required=True,
                type=str,
                location=OpenApiParameter.QUERY
            ),
            OpenApiParameter(
                name="artist_id",
                description="ID of the artist",
                required=True,
                type=int,
                location=OpenApiParameter.QUERY
            ),
            OpenApiParameter(
                name="singer",
                description="Singer of the music",
                required=True,
                type=str,
                location=OpenApiParameter.QUERY
            ),
            OpenApiParameter(
                name="writer",
                description="Writer of the music",
                required=True,
                type=str,
                location=OpenApiParameter.QUERY
            ),
            OpenApiParameter(
                name="description",
                description="Music description",
                required=False,
                type=str,
                location=OpenApiParameter.QUERY
            ),
            OpenApiParameter(
                name="released_date",
                description="Release date (YYYY-MM-DD)",
                required=False,
                type=str,
                location=OpenApiParameter.QUERY
            ),
        ]
