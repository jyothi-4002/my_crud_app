from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create),
    path("get_all/", views.get_all),
    path("get/<int:todo_id>/", views.get),
    path("update/<int:todo_id>/", views.update),
    path("delete/<int:todo_id>/", views.delete),
]
