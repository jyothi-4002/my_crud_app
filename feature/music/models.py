from django.db import models
from django.utils import timezone
from feature.artist.models import Artist
from feature.music.dataclasses.request.create import MusicCreateRequest
from feature.music.dataclasses.request.update import MusicUpdateRequest

class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs")
    singer = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    released_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "music"
        ordering = ["-created_at"]

    @classmethod
    def create_item(cls, data: MusicCreateRequest):
        artist = Artist.get_item(data.artist_id)
        if not artist:
            raise ValueError("Artist not found")

        return cls.objects.create(
            title=data.title,
            artist=artist,
            singer=data.singer,
            writer=data.writer,
            description=data.description,
            released_date=data.released_date,
        )

    @classmethod
    def get_item(cls, music_id: int):
        return cls.objects.filter(id=music_id).select_related("artist").first()

    @classmethod
    def get_all_items(cls):
        return cls.objects.select_related("artist").all()

    @classmethod
    def delete_item(cls, music_id: int):
        obj = cls.get_item(music_id)
        if not obj:
            return False
        obj.delete()
        return True

    @staticmethod
    def to_response(obj):
        return {
            "id": obj.id,
            "title": obj.title,
            "singer": obj.singer,
            "writer": obj.writer,
            "description": obj.description,
            "released_date": obj.released_date,
            "createdAt": obj.created_at,
            "artist": {
                "id": obj.artist.id,
                "name": obj.artist.name,
                "age": obj.artist.age,
            }
        }
