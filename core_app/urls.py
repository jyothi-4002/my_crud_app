# core_app/urls.py
from django.urls import path, include
from core_app import views as core_views  # if you have hello/hai

urlpatterns = [
    path("", include([
        path("hello/", core_views.hello, name='hello'),
        path("hai/", core_views.hai, name='hai'),
    ])),
    path("todo/", include('core_app.todo.urls')),
]
