from rest_framework import serializers
from drf_spectacular.utils import OpenApiParameter
from feature.music.dataclasses.request.update import MusicUpdateRequest

class MusicUpdateRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(required=False)
    artist_id = serializers.IntegerField(required=False)
    singer = serializers.CharField(required=False)
    writer = serializers.CharField(required=False)
    description = serializers.CharField(required=False)

    def create(self, validated_data):
        return MusicUpdateRequest(**validated_data)

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
