from rest_framework import serializers


class ArtistDeleteResponseSerializer(serializers.Serializer):
    deleted_ids = serializers.ListField(
        child=serializers.IntegerField()
    )
