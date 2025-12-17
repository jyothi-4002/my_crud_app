from django.urls import path
from core_app.feature.music import controller

urlpatterns = [
    path("create/", controller.create_music),
    path("get/", controller.get_music),
    path("get-all/", controller.get_all_music),
    path("update/", controller.update_music),
    path("delete/", controller.delete_music),
]
