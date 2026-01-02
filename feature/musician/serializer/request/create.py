from rest_framework import serializers
from feature.musician.dataclasses.request.create import MusicianCreateDC


class MusicianCreateRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()

    def create(self, validated_data):
        return MusicianCreateDC(
            name=validated_data["name"],
            age=validated_data["age"]
        )
