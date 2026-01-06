from rest_framework import serializers


class ArtistGetAllItemResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    description = serializers.CharField(allow_null=True)
    debut_date = serializers.DateField(allow_null=True)
    createdAt = serializers.DateTimeField()


class ArtistGetAllResponseSerializer(serializers.Serializer):
    data = ArtistGetAllItemResponseSerializer(many=True)
    presentPage = serializers.IntegerField()
    totalPage = serializers.IntegerField()
    totalCount = serializers.IntegerField()
    nextPageUrl = serializers.CharField(required=False, allow_null=True)
