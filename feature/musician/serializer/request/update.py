from rest_framework import serializers
from feature.musician.dataclasses.request.update import MusicianUpdateDC


class MusicianUpdateRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return MusicianUpdateDC(
            id=validated_data["id"],
            name=validated_data.get("name"),
            age=validated_data.get("age")
        )
