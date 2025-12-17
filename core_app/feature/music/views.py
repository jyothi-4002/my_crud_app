from django.core.paginator import Paginator
from core_app.feature.music.models import Music


class MusicView:

    def create(self, params):
        obj = Music.create_item(**params.__dict__)
        return Music.to_response(obj)

    def get(self, params):
        obj = Music.get_item(params.id)
        if not obj:
            raise ValueError("Music not found")
        return Music.to_response(obj)

    def get_all(self, params, request):
        qs = Music.get_all_items()
        paginator = Paginator(qs, params.limit)
        page = paginator.page(params.page_num)

        data = [Music.to_response(o) for o in page.object_list]

        return {
            "data": data,
            "presentPage": params.page_num,
            "totalPage": paginator.num_pages,
            "totalCount": paginator.count,
        }

    def update(self, params):
        obj = Music.get_item(params.id)
        if not obj:
            raise ValueError("Music not found")

        for k, v in params.__dict__.items():
            if k != "id" and v is not None:
                setattr(obj, k, v)

        obj.save()
        return Music.to_response(obj)

    def delete(self, params):
        deleted_ids = []
        for mid in params.ids:
            if Music.delete_item(mid):
                deleted_ids.append(mid)
        return {"deleted_ids": deleted_ids}
