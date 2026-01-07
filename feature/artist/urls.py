from django.urls import path
from . import controller

urlpatterns = [
    path("create/", controller.ArtistController.create),
    path("get/", controller.ArtistController.get),
    path("get-all/", controller.ArtistController.get_all),
    path("update/", controller.ArtistController.update),
    path("delete/", controller.ArtistController.delete),
]
