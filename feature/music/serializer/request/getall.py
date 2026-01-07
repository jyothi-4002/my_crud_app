from rest_framework import serializers
from drf_spectacular.utils import OpenApiParameter
from feature.music.dataclasses.request.getall import MusicGetAllRequest

class MusicGetAllRequestSerializer(serializers.Serializer):
    page_num = serializers.IntegerField(required=False, default=1)
    limit = serializers.IntegerField(required=False, default=10)

    def create(self, validated_data):
        return MusicGetAllRequest(**validated_data)

    @staticmethod
    def get_all_parameters():
        return [
            OpenApiParameter(
                name="page_num",
                description="Page number",
                required=False,
                type=int,
                location=OpenApiParameter.QUERY
            ),
            OpenApiParameter(
                name="limit",
                description="Items per page",
                required=False,
                type=int,
                location=OpenApiParameter.QUERY
            )
        ]
