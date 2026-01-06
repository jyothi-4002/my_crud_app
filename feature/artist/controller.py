from rest_framework.decorators import api_view
from common.swagger import SwaggerUtils
from drf_yasg import openapi

from feature.artist.views import ArtistView
from common.utils import CommonUtils

from feature.artist.serializer.request.create import ArtistCreateRequestSerializer
from feature.artist.serializer.request.get import ArtistGetRequestSerializer
from feature.artist.serializer.request.getall import ArtistGetAllRequestSerializer
from feature.artist.serializer.request.update import ArtistUpdateRequestSerializer
from feature.artist.serializer.request.delete import ArtistDeleteRequestSerializer

artist_view = ArtistView()

@SwaggerUtils.create_endpoint(ArtistCreateRequestSerializer, description="Create a new artist")

@api_view(["POST"])
def create_artist(request):
    serializer = ArtistCreateRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return artist_view.create(serializer.save())

@SwaggerUtils.get_endpoint(
    query_params=[{"name": "id", "type": openapi.TYPE_INTEGER, "required": True, "description": "Artist ID"}],
    description="Get an artist by ID"
)

@api_view(["GET"])
def get_artist(request):
    params = CommonUtils.get_query_params(request)
    serializer = ArtistGetRequestSerializer(data=params)
    serializer.is_valid(raise_exception=True)
    return artist_view.get(serializer.save())

@SwaggerUtils.get_endpoint(
    query_params=[{"name": "page_num", "type": openapi.TYPE_INTEGER, "required": False, "description": "Page number"}],
    description="Get all artists"
)

@api_view(["GET"])
def get_all_artist(request):
    params = CommonUtils.get_query_params(request)
    serializer = ArtistGetAllRequestSerializer(data=params)
    serializer.is_valid(raise_exception=True)
    return artist_view.get_all(serializer.save(), request)

@SwaggerUtils.update_endpoint(
    ArtistUpdateRequestSerializer,
    query_params=[{"name": "id", "type": openapi.TYPE_INTEGER, "required": True, "description": "Artist ID"}],
    description="Update artist by ID"
)

@api_view(["PUT"])
def update_artist(request):
    params = CommonUtils.get_query_params(request)
    data = request.data.copy()
    data["id"] = int(params["id"])

    serializer = ArtistUpdateRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return artist_view.update(serializer.save())

@SwaggerUtils.delete_endpoint(
    query_params=[{"name": "ids", "type": openapi.TYPE_STRING, "required": True, "description": "Comma-separated artist IDs"}],
    description="Delete artist(s)"
)
@api_view(["DELETE"])
def delete_artist(request):
    params = CommonUtils.get_query_params(request)

    raw_ids = params.get("ids", [])
    ids = [int(i) for i in raw_ids]

    serializer = ArtistDeleteRequestSerializer(data={"ids": ids})
    serializer.is_valid(raise_exception=True)
    return artist_view.delete(serializer.save())

