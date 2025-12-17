from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from core_app.feature.music.views import MusicView
from core_app.feature.music.utils import MusicUtils

from core_app.feature.music.serializer.request.create import MusicCreateRequestSerializer
from core_app.feature.music.serializer.request.get import MusicGetRequestSerializer
from core_app.feature.music.serializer.request.getall import MusicGetAllRequestSerializer
from core_app.feature.music.serializer.request.update import MusicUpdateRequestSerializer
from core_app.feature.music.serializer.request.delete import MusicDeleteRequestSerializer

music_view = MusicView()


@api_view(["POST"])
def create_music(request):
    serializer = MusicCreateRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    result = music_view.create(serializer.save())

    return Response(
        MusicUtils.success_response_data("Music created", result),
        status=status.HTTP_201_CREATED
    )


@api_view(["GET"])
def get_music(request):
    params = MusicUtils.get_query_params(request)
    serializer = MusicGetRequestSerializer(data=params)
    serializer.is_valid(raise_exception=True)

    result = music_view.get(serializer.save())
    return Response(MusicUtils.success_response_data(data=result))


@api_view(["GET"])
def get_all_music(request):
    params = MusicUtils.get_query_params(request)
    serializer = MusicGetAllRequestSerializer(data=params)
    serializer.is_valid(raise_exception=True)

    result = music_view.get_all(serializer.save(), request)
    return Response(MusicUtils.success_response_data(data=result))


@api_view(["PUT"])
def update_music(request):
    params = MusicUtils.get_query_params(request)
    data = request.data.copy()
    data["id"] = int(params["id"])

    serializer = MusicUpdateRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    result = music_view.update(serializer.save())
    return Response(MusicUtils.success_response_data(data=result))


@api_view(["DELETE"])
def delete_music(request):
    params = MusicUtils.get_query_params(request)
    ids = [int(i) for i in params.get("ids", "").split(",") if i]

    serializer = MusicDeleteRequestSerializer(data={"ids": ids})
    serializer.is_valid(raise_exception=True)

    result = music_view.delete(serializer.save())
    return Response(MusicUtils.success_response_data(data=result))
