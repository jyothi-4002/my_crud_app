from django.core.paginator import Paginator
from feature.musician.models import Musician
from common.utils import CommonUtils


class MusicianView:

    def create(self, dc):
        obj = Musician.create_item(dc.name, dc.age)
        return CommonUtils.success_response_data(
            message="Musician created",
            data=Musician.to_response(obj)
        )

    def get(self, dc):
        obj = Musician.get_item(dc.id)
        if not obj:
            return CommonUtils.error_response_data("Musician not found")

        return CommonUtils.success_response_data(
            data=Musician.to_response(obj)
        )

    def get_all(self, dc):
        qs = Musician.get_all_items()
        paginator = Paginator(qs, dc.limit)
        page = paginator.page(dc.page_num)

        data = [Musician.to_response(o) for o in page.object_list]

        return CommonUtils.success_response_data(
            data={
                "data": data,
                "presentPage": dc.page_num,
                "totalPage": paginator.num_pages,
                "totalCount": paginator.count,
            }
        )

    def update(self, dc):
        obj = Musician.get_item(dc.id)
        if not obj:
            return CommonUtils.error_response_data("Musician not found")

        obj.update_item(dc.name, dc.age)

        return CommonUtils.success_response_data(
            message="Musician updated",
            data=Musician.to_response(obj)
        )

    def delete(self, dc):
        deleted_ids = []

        for musician_id in dc.ids:
            if Musician.delete_item(musician_id):
                deleted_ids.append(musician_id)

        return CommonUtils.success_response_data(
            message="Musician deleted",
            data={"deleted_ids": deleted_ids}
        )
