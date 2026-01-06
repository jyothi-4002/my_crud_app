from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework import status

from feature.artist.models import Artist
from feature.artist.utils import ArtistUtils


class ArtistView:

    def create(self, params):
        obj = Artist.create_item(params)
        return Response(
            ArtistUtils.success_response_data(data=Artist.to_response(obj)),
            status=status.HTTP_201_CREATED
        )

    def get(self, params):
        obj = Artist.get_item(params.id)
        if not obj:
            return Response(
                ArtistUtils.error_response_data("Artist not found"),
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            ArtistUtils.success_response_data(data=Artist.to_response(obj))
        )

    def get_all(self, params, request):
        qs = Artist.get_all_items()
        paginator = Paginator(qs, params.limit)
        page = paginator.page(params.page_num)

        data = [Artist.to_response(o) for o in page.object_list]

        response_data = {
            "data": data,
            "presentPage": params.page_num,
            "totalPage": paginator.num_pages,
            "totalCount": paginator.count,
        }

        return Response(
            ArtistUtils.success_response_data(data=response_data)
        )

    def update(self, params):
        obj = Artist.get_item(params.id)
        if not obj:
            return Response(
                ArtistUtils.error_response_data("Artist not found"),
                status=status.HTTP_404_NOT_FOUND
            )

        for k, v in params.__dict__.items():
            if k != "id" and v is not None:
                setattr(obj, k, v)

        obj.save()

        return Response(
            ArtistUtils.success_response_data(data=Artist.to_response(obj))
        )

    def delete(self, params):
        deleted_ids = []

        for aid in params.ids:
            if Artist.delete_item(aid):
                deleted_ids.append(aid)

        return Response(
            ArtistUtils.success_response_data(
                data={"deleted_ids": deleted_ids}
            )
        )
