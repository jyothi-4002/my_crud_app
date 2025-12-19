from feature.todo.dataclasses.response.update import TodoUpdateResponse

from rest_framework import serializers

class TodoUpdateResponseSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField(allow_blank=True)
    isCompleted = serializers.BooleanField()
    createdDateTime = serializers.DateTimeField()
    isActive = serializers.BooleanField()
    createdBy = serializers.CharField(allow_null=True)
    createdBranch = serializers.CharField(allow_null=True)
    createdByCode = serializers.CharField(allow_null=True)
    createdBranchCode = serializers.CharField(allow_null=True)


    def create(self, validated_data) -> TodoUpdateResponse:
        return TodoUpdateResponse(**validated_data)

