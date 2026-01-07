from rest_framework import serializers
from drf_spectacular.utils import OpenApiParameter
from feature.music.dataclasses.request.delete import MusicDeleteRequest

class MusicDeleteRequestSerializer(serializers.Serializer):
    ids = serializers.ListField(child=serializers.IntegerField(), allow_empty=False)

    def create(self, validated_data):
        return MusicDeleteRequest(**validated_data)

    @staticmethod
    def get_parameters():
        return [
            OpenApiParameter(
                name="ids",
                description="Comma-separated music IDs",
                required=True,
                type=str,
                location=OpenApiParameter.QUERY
            )
        ]
