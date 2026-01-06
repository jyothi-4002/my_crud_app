from rest_framework.decorators import api_view

from feature.artist.views import ArtistView
from feature.artist.utils import ArtistUtils

from feature.artist.serializer.request.create import ArtistCreateRequestSerializer
from feature.artist.serializer.request.get import ArtistGetRequestSerializer
from feature.artist.serializer.request.getall import ArtistGetAllRequestSerializer
from feature.artist.serializer.request.update import ArtistUpdateRequestSerializer
from feature.artist.serializer.request.delete import ArtistDeleteRequestSerializer

artist_view = ArtistView()


@api_view(["POST"])
def create_artist(request):
    serializer = ArtistCreateRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return artist_view.create(serializer.save())


@api_view(["GET"])
def get_artist(request):
    params = ArtistUtils.get_query_params(request)
    serializer = ArtistGetRequestSerializer(data=params)
    serializer.is_valid(raise_exception=True)
    return artist_view.get(serializer.save())


@api_view(["GET"])
def get_all_artist(request):
    params = ArtistUtils.get_query_params(request)
    serializer = ArtistGetAllRequestSerializer(data=params)
    serializer.is_valid(raise_exception=True)
    return artist_view.get_all(serializer.save(), request)


@api_view(["PUT"])
def update_artist(request):
    params = ArtistUtils.get_query_params(request)
    data = request.data.copy()
    data["id"] = int(params["id"])

    serializer = ArtistUpdateRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return artist_view.update(serializer.save())


@api_view(["DELETE"])
def delete_artist(request):
    params = ArtistUtils.get_query_params(request)

    raw_ids = params.get("ids", [])
    ids = [int(i) for i in raw_ids]

    serializer = ArtistDeleteRequestSerializer(data={"ids": ids})
    serializer.is_valid(raise_exception=True)
    return artist_view.delete(serializer.save())

