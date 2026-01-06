from rest_framework import serializers
from feature.artist.dataclasses.request.create import ArtistCreateRequest

class ArtistCreateRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    description = serializers.CharField(required=False, allow_blank=True)
    debut_date = serializers.DateField(required=False)

    def create(self, validated_data):
        return ArtistCreateRequest(**validated_data)