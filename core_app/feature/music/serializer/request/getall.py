from rest_framework import serializers
from core_app.feature.music.dataclasses.request.getall import MusicGetAllRequest

class MusicGetAllRequestSerializer(serializers.Serializer):
    page_num = serializers.IntegerField(required=False, default=1)
    limit = serializers.IntegerField(required=False, default=10)

    def create(self, validated_data):
        return MusicGetAllRequest(**validated_data)
