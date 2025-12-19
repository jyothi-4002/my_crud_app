from rest_framework import serializers
from feature.music.dataclasses.request.create import MusicCreateRequest

class MusicCreateRequestSerializer(serializers.Serializer):
    title = serializers.CharField()
    singer = serializers.CharField()
    writer = serializers.CharField()
    description = serializers.CharField(required=False, allow_blank=True)
    released_date = serializers.DateField(required=False)

    def create(self, validated_data):
        return MusicCreateRequest(**validated_data)
