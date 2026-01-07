from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from feature.music.views import MusicView
from common.utils import CommonUtils

from feature.music.serializer.request.create import MusicCreateRequestSerializer
from feature.music.serializer.request.get import MusicGetRequestSerializer
from feature.music.serializer.request.getall import MusicGetAllRequestSerializer
from feature.music.serializer.request.update import MusicUpdateRequestSerializer
from feature.music.serializer.request.delete import MusicDeleteRequestSerializer


class MusicController:

    @staticmethod
    @extend_schema(
        description="Create a new music record",
        request=MusicCreateRequestSerializer,
        parameters=MusicCreateRequestSerializer.get_parameters()
    )
    @api_view(["POST"])
    def create(request: Request) -> Response:
        serializer = MusicCreateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return MusicView().create(serializer.save())

    @staticmethod
    @extend_schema(
        description="Get music by ID",
        parameters=MusicGetRequestSerializer.get_parameters()
    )
    @api_view(["GET"])
    def get(request: Request) -> Response:
        params = CommonUtils.get_query_params(request)
        serializer = MusicGetRequestSerializer(data=params)
        serializer.is_valid(raise_exception=True)
        return MusicView().get(serializer.save())

    @staticmethod
    @extend_schema(
        description="Get all music records",
        parameters=MusicGetAllRequestSerializer.get_all_parameters()
    )
    @api_view(["GET"])
    def get_all(request: Request) -> Response:
        params = CommonUtils.get_query_params(request)
        serializer = MusicGetAllRequestSerializer(data=params)
        serializer.is_valid(raise_exception=True)
        return MusicView().get_all(serializer.save(), request)

    @staticmethod
    @extend_schema(
        description="Update music by ID",
        request=MusicUpdateRequestSerializer,
        parameters=MusicUpdateRequestSerializer.get_parameters()
    )
    @api_view(["PUT"])
    def update(request: Request) -> Response:
        params = CommonUtils.get_query_params(request)
        data = request.data.copy()
        data["id"] = int(params["id"])

        serializer = MusicUpdateRequestSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return MusicView().update(serializer.save())

    @staticmethod
    @extend_schema(
        description="Delete music records",
        parameters=MusicDeleteRequestSerializer.get_parameters()
    )
    @api_view(["DELETE"])
    def delete(request: Request) -> Response:
        params = CommonUtils.get_query_params(request)
        ids = [int(i) for i in params.get("ids", "").split(",") if i]

        serializer = MusicDeleteRequestSerializer(data={"ids": ids})
        serializer.is_valid(raise_exception=True)
        return MusicView().delete(serializer.save())
