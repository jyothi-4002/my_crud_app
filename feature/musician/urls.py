from django.urls import path
from feature.music.controller import *

urlpatterns = [
    path("create/", create_music),
    path("get/", get_music),
    path("get-all/", get_all_music),
    path("update/", update_music),
    path("delete/", delete_music),
]
