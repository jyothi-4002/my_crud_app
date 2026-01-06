from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version="v1",
        description="Artist, Music, Todo APIs",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # feature urls
    path("music/", include("feature.music.urls")),
    path("todo/", include("feature.todo.urls")),
    path("artist/", include("feature.artist.urls")),

    # swagger (COMMON)
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
]
