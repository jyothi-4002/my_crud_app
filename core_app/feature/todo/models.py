# core_app/todo/models.py
from django.db import models
from django.utils import timezone

class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "todo"

    @classmethod
    def create_item(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def get_all_items(cls):
        return cls.objects.all().order_by("-created_at")

    @classmethod
    def get_item(cls, todo_id):
        try:
            return cls.objects.get(id=todo_id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def delete_item(cls, todo_id):
        obj = cls.get_item(todo_id)
        if not obj:
            return False
        obj.delete()
        return True

    @staticmethod
    def to_response(obj):
        return {
            "id": obj.id,
            "title": obj.title,
            "description": obj.description or "",
            "isCompleted": obj.completed,
            "createdDateTime": obj.created_at.isoformat(),
            "isActive": True,
            "createdBy": "System User",
            "createdBranch": None,
            "createdByCode": "SYS",
            "createdBranchCode": None,
        }
