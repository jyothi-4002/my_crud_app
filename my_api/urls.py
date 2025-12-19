# my_api/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("music/", include("feature.music.urls")),
    path("todo/", include("feature.todo.urls")),
    # only include core_app once
]
