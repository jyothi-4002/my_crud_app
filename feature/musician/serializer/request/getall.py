from rest_framework import serializers
from feature.musician.dataclasses.request.getall import MusicianGetAllDC


class MusicianGetAllRequestSerializer(serializers.Serializer):
    page_num = serializers.IntegerField(default=1)
    limit = serializers.IntegerField(default=10)

    def create(self, validated_data):
        return MusicianGetAllDC(
            page_num=validated_data.get("page_num", 1),
            limit=validated_data.get("limit", 10)
        )
