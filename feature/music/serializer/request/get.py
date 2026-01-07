from rest_framework import serializers
from drf_spectacular.utils import OpenApiParameter
from feature.music.dataclasses.request.get import MusicGetRequest

class MusicGetRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def create(self, validated_data):
        return MusicGetRequest(**validated_data)

    @staticmethod
    def get_parameters():
        return [
            OpenApiParameter(
                name="id",
                description="Music ID",
                required=True,
                type=int,
                location=OpenApiParameter.QUERY
            )
        ]
