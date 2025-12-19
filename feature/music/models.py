from django.db import models
from django.utils import timezone
from feature.music.dataclasses.request.create import MusicCreateRequest
from feature.music.dataclasses.request.update import MusicUpdateRequest







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

    # database

    @classmethod
    def create_item(cls, data: MusicCreateRequest):
        return cls.objects.create(
            title=data.title,
            singer=data.singer,
            writer=data.writer,
            description=data.description,
            released_date=data.released_date,
        )

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
    def update_item(cls, data: MusicUpdateRequest):
        """
        Update music record using dataclass (NO kwargs)
        """
        obj = cls.get_item(data.id)
        if not obj:
            return None

        if data.title is not None:
            obj.title = data.title
        if data.singer is not None:
            obj.singer = data.singer
        if data.writer is not None:
            obj.writer = data.writer
        if data.description is not None:
            obj.description = data.description
        if data.released_date is not None:
            obj.released_date = data.released_date

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

# response mapper
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
