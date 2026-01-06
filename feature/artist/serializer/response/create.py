from rest_framework import serializers


class ArtistCreateResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    description = serializers.CharField(allow_null=True)
    debut_date = serializers.DateField(allow_null=True)
    createdAt = serializers.DateTimeField()
