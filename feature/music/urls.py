from django.urls import path
from .controller import MusicController

urlpatterns = [
    path("create/", MusicController.create),
    path("get/", MusicController.get),
    path("get-all/", MusicController.get_all),
    path("update/", MusicController.update),
    path("delete/", MusicController.delete),
]
