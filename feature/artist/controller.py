from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from feature.artist.views import ArtistView
from common.utils import CommonUtils

from feature.artist.serializer.request.create import ArtistCreateRequestSerializer
from feature.artist.serializer.request.get import ArtistGetRequestSerializer
from feature.artist.serializer.request.getall import ArtistGetAllRequestSerializer
from feature.artist.serializer.request.update import ArtistUpdateRequestSerializer
from feature.artist.serializer.request.delete import ArtistDeleteRequestSerializer


class ArtistController:

    # ---------- CREATE ----------
    @staticmethod
    @api_view(["POST"])
    @extend_schema(
        description="Create artist",
        request=ArtistCreateRequestSerializer
    )
    def create(request: Request) -> Response:
        serializer = ArtistCreateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return ArtistView().create(serializer.save())

    # ---------- GET ----------
    @staticmethod
    @api_view(["GET"])
    @extend_schema(
        description="Get artist by ID",
        parameters=ArtistGetRequestSerializer.get_parameters()
    )
    def get(request: Request) -> Response:
        params = CommonUtils.get_query_params(request)
        serializer = ArtistGetRequestSerializer(data=params)
        serializer.is_valid(raise_exception=True)
        return ArtistView().get(serializer.save())

    # ---------- GET ALL ----------
    @staticmethod
    @api_view(["GET"])
    @extend_schema(
        description="Get all artists",
        parameters=ArtistGetAllRequestSerializer.get_all_parameters()
    )
    def get_all(request: Request) -> Response:
        params = CommonUtils.get_query_params(request)
        serializer = ArtistGetAllRequestSerializer(data=params)
        serializer.is_valid(raise_exception=True)
        return ArtistView().get_all(serializer.save(), request)

    # ---------- UPDATE ----------
    @staticmethod
    @api_view(["PUT"])
    @extend_schema(
        description="Update artist",
        request=ArtistUpdateRequestSerializer,
        parameters=ArtistUpdateRequestSerializer.get_parameters()
    )
    def update(request: Request) -> Response:
        params = CommonUtils.get_query_params(request)
        data = request.data.copy()
        data["id"] = int(params["id"])

        serializer = ArtistUpdateRequestSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return ArtistView().update(serializer.save())

    # ---------- DELETE ----------
    @staticmethod
    @api_view(["DELETE"])
    @extend_schema(
        description="Delete artists",
        parameters=ArtistDeleteRequestSerializer.get_parameters()
    )
    def delete(request: Request) -> Response:
        params = CommonUtils.get_query_params(request)
        ids = [int(i) for i in params["ids"].split(",")]

        serializer = ArtistDeleteRequestSerializer(data={"ids": ids})
        serializer.is_valid(raise_exception=True)
        return ArtistView().delete(serializer.save())
