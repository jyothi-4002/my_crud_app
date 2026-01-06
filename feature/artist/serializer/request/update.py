from rest_framework import serializers
from feature.artist.dataclasses.request.update import ArtistUpdateRequest

class ArtistUpdateRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    description = serializers.CharField(required=False)
    debut_date = serializers.DateField(required=False)

    def create(self, validated_data):
        return ArtistUpdateRequest(**validated_data)
