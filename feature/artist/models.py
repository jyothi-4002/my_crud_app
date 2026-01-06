from django.db import models
from django.utils import timezone
from feature.artist.dataclasses.request.create import ArtistCreateRequest

class Artist(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    debut_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "artist"
        ordering = ["-created_at"]

    @classmethod
    def create_item(cls, data: ArtistCreateRequest):
        return cls.objects.create(
            name=data.name,
            age=data.age,
            description=data.description,
            debut_date=data.debut_date,
        )

    @classmethod
    def get_item(cls, artist_id: int):
        return cls.objects.filter(id=artist_id).first()

    @classmethod
    def get_all_items(cls):
        return cls.objects.all()

    @classmethod
    def delete_item(cls, artist_id: int):
        obj = cls.get_item(artist_id)
        if not obj:
            return False
        obj.delete()
        return True

    @staticmethod
    def to_response(obj):
        return {
            "id": obj.id,
            "name": obj.name,
            "age": obj.age,
            "description": obj.description,
            "debut_date": obj.debut_date,
            "createdAt": obj.created_at,
        }
