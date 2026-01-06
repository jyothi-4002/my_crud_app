from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework import status

from feature.music.models import Music
from common.utils import CommonUtils


class MusicView:

    def create(self, params):
        obj = Music.create_item(params)
        data = Music.to_response(obj)

        return Response(
            CommonUtils.success_response_data(data=data),
            status=status.HTTP_201_CREATED
        )

    def get(self, params):
        obj = Music.get_item(params.id)
        if not obj:
            return Response(
                CommonUtils.error_response_data("Music not found"),
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            CommonUtils.success_response_data(
                data=Music.to_response(obj)
            )
        )

    def get_all(self, params, request):
        qs = Music.get_all_items()
        paginator = Paginator(qs, params.limit)
        page = paginator.page(params.page_num)

        data = [Music.to_response(o) for o in page.object_list]

        response_data = {
            "data": data,
            "presentPage": params.page_num,
            "totalPage": paginator.num_pages,
            "totalCount": paginator.count,
        }

        return Response(
            CommonUtils.success_response_data(data=response_data)
        )

    def update(self, params):
        obj = Music.get_item(params.id)
        if not obj:
            return Response(
                CommonUtils.error_response_data("Music not found"),
                status=status.HTTP_404_NOT_FOUND
            )

        for k, v in params.__dict__.items():
            if k != "id" and v is not None:
                setattr(obj, k, v)

        obj.save()

        return Response(
            CommonUtils.success_response_data(
                data=Music.to_response(obj)
            )
        )

    def delete(self, params):
        deleted_ids = []

        for mid in params.ids:
            if Music.delete_item(mid):
                deleted_ids.append(mid)

        return Response(
            CommonUtils.success_response_data(
                data={"deleted_ids": deleted_ids}
            )
        )
