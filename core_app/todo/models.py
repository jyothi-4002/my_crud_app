from django.db import models
from django.utils import timezone
from typing import Optional, List, Dict


class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        db_table = "todo"

    @classmethod
    def create_item(cls, title: str, description: str = "", completed: bool = False) -> "TodoItem":
        return cls.objects.create(title=title, description=description, completed=completed)

    @classmethod
    def get_all_items(cls) -> List[Dict]:
        return list(cls.objects.all().order_by("-created_at").values())

    @classmethod
    def get_item_by_id(cls, todo_id: int) -> Optional[Dict]:
        try:
            obj = cls.objects.get(id=todo_id)
            return cls._to_dict(obj)
        except cls.DoesNotExist:
            return None

    @classmethod
    def update_item(cls, todo_id: int, title=None, description=None, completed=None) -> Optional[Dict]:
        try:
            obj = cls.objects.get(id=todo_id)
        except cls.DoesNotExist:
            return None
        if title is not None:
            obj.title = title
        if description is not None:
            obj.description = description
        if completed is not None:
            obj.completed = completed
        obj.save()
        return cls._to_dict(obj)

    @classmethod
    def delete_item(cls, todo_id: int) -> bool:
        try:
            obj = cls.objects.get(id=todo_id)
        except cls.DoesNotExist:
            return False
        obj.delete()
        return True

    @staticmethod
    def _to_dict(obj: "TodoItem") -> Dict:
        return {
            "id": obj.id,
            "title": obj.title,
            "description": obj.description or "",
            "completed": obj.completed,
            "created_at": obj.created_at.isoformat(),
            "updated_at": obj.updated_at.isoformat(),
        }
