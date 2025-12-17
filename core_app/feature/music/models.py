from django.db import models
from django.utils import timezone


class Music(models.Model):
    title = models.CharField(max_length=255)
    singer = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    released_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "music"
        ordering = ["-created_at"]

    # -------------------- DATABASE OPERATIONS -------------------- #

    @classmethod
    def create_item(cls, **kwargs):
        """
        Create music record
        """
        return cls.objects.create(**kwargs)

    @classmethod
    def get_item(cls, music_id: int):
        """
        Get single music by id
        """
        try:
            return cls.objects.get(id=music_id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_all_items(cls):
        """
        Get all music records
        """
        return cls.objects.all()

    @classmethod
    def update_item(cls, music_id: int, **kwargs):
        """
        Update music fields
        """
        obj = cls.get_item(music_id)
        if not obj:
            return None

        for key, value in kwargs.items():
            setattr(obj, key, value)

        obj.save()
        return obj

    @classmethod
    def delete_item(cls, music_id: int) -> bool:
        """
        Delete music record
        """
        obj = cls.get_item(music_id)
        if not obj:
            return False

        obj.delete()
        return True

    # -------------------- RESPONSE MAPPER -------------------- #

    @staticmethod
    def to_response(obj) -> dict:
        """
        Convert model to response dict
        (used by dataclass responses)
        """
        return {
            "id": obj.id,
            "title": obj.title,
            "singer": obj.singer,
            "writer": obj.writer,
            "description": obj.description or "",
            "released_date": obj.released_date.isoformat()
            if obj.released_date else None,
            "createdAt": obj.created_at.isoformat(),
        }
