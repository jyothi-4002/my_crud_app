# core_app/urls.py
from django.urls import path, include
from core_app import views as core_views

urlpatterns = [
    path("hello/", core_views.hello, name='hello'),
    path("hai/", core_views.hai, name='hai'),
    path("todo/", include("core_app.feature.todo.urls")),
    path("music/", include("core_app.feature.music.urls")),
    # include the todo URLs correctly
]
