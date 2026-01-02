from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.utils import CommonUtils
from feature.musician.views import MusicianView
from feature.musician.serializer.request.create import MusicianCreateRequestSerializer
from feature.musician.serializer.request.get import MusicianGetRequestSerializer
from feature.musician.serializer.request.getall import MusicianGetAllRequestSerializer
from feature.musician.serializer.request.update import MusicianUpdateRequestSerializer
from feature.musician.serializer.request.delete import MusicianDeleteRequestSerializer

musician_view = MusicianView()


@api_view(["POST"])
def create_musician(request):
    serializer = MusicianCreateRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    result = musician_view.create(serializer.save())
    return Response(result)


@api_view(["GET"])
def get_musician(request):
    params = CommonUtils.get_query_params(request)
    serializer = MusicianGetRequestSerializer(data=params)
    serializer.is_valid(raise_exception=True)

    result = musician_view.get(serializer.save())
    return Response(result)


@api_view(["GET"])
def get_all_musician(request):
    params = CommonUtils.get_query_params(request)
    serializer = MusicianGetAllRequestSerializer(data=params)
    serializer.is_valid(raise_exception=True)

    result = musician_view.get_all(serializer.save())
    return Response(result)


@api_view(["PUT"])
def update_musician(request):
    params = CommonUtils.get_query_params(request)
    data = request.data.copy()
    data["id"] = int(params["id"])

    serializer = MusicianUpdateRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    result = musician_view.update(serializer.save())
    return Response(result)


@api_view(["DELETE"])
def delete_musician(request):
    params = CommonUtils.get_query_params(request)

