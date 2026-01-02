from django.db import models


class Musician(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    class Meta:
        db_table = "musician"

    @classmethod
    def create_item(cls, name: str, age: int):
        obj = cls(name=name, age=age)
        obj.save()
        return obj

    @classmethod
    def get_item(cls, musician_id: int):
        return cls.objects.filter(id=musician_id).first()

    @classmethod
    def get_all_items(cls):
        return cls.objects.all().order_by("id")

    def update_item(self, name=None, age=None):
        if name is not None:
            self.name = name
        if age is not None:
            self.age = age
        self.save()
        return self

    @classmethod
    def delete_item(cls, musician_id: int):
        obj = cls.get_item(musician_id)
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
        }
