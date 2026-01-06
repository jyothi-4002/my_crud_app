from rest_framework.decorators import api_view
from common.swagger import SwaggerUtils
from feature.music.views import MusicView
from common.utils import CommonUtils
from drf_yasg import openapi


from feature.music.serializer.request.create import MusicCreateRequestSerializer
from feature.music.serializer.request.get import MusicGetRequestSerializer
from feature.music.serializer.request.getall import MusicGetAllRequestSerializer
from feature.music.serializer.request.update import MusicUpdateRequestSerializer
from feature.music.serializer.request.delete import MusicDeleteRequestSerializer


music_view = MusicView()

@SwaggerUtils.create_endpoint(MusicCreateRequestSerializer, description="Create a new music record")
@api_view(["POST"])
def create_music(request):
    serializer = MusicCreateRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    return music_view.create(serializer.save())

@SwaggerUtils.get_endpoint(
    query_params=[{"name": "id", "type": "integer", "required": True, "description": "Music ID"}],
    description="Get music by ID"
)
@api_view(["GET"])
def get_music(request):
    params = CommonUtils.get_query_params(request)
    serializer = MusicGetRequestSerializer(data=params)
    serializer.is_valid(raise_exception=True)

    return music_view.get(serializer.save())

@SwaggerUtils.get_endpoint(
    query_params=[{"name": "page_num", "type": "integer", "required": False, "description": "Page number"}],
    description="Get all music records"
)
@api_view(["GET"])
def get_all_music(request):
    params = CommonUtils.get_query_params(request)
    serializer = MusicGetAllRequestSerializer(data=params)
    serializer.is_valid(raise_exception=True)

    return music_view.get_all(serializer.save(), request)

@SwaggerUtils.update_endpoint(
    MusicUpdateRequestSerializer,
    query_params=[{"name": "id", "type": "integer", "required": True, "description": "Music ID"}],
    description="Update music by ID"
)
@api_view(["PUT"])
def update_music(request):
    params = CommonUtils.get_query_params(request)
    data = request.data.copy()
    data["id"] = int(params["id"])

    serializer = MusicUpdateRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    return music_view.update(serializer.save())

@SwaggerUtils.delete_endpoint(
    query_params=[{"name": "ids", "type": "string", "required": True, "description": "Comma-separated music IDs"}],
    description="Delete music(s)"
)
@api_view(["DELETE"])
def delete_music(request):
    params = CommonUtils.get_query_params(request)
    ids = [int(i) for i in params.get("ids", "").split(",") if i]

    serializer = MusicDeleteRequestSerializer(data={"ids": ids})
    serializer.is_valid(raise_exception=True)

    return music_view.delete(serializer.save())
