# core_app/todo/urls.py
from django.urls import path
from feature.todo import controller

urlpatterns = [
    path("create/", controller.create_todo, name="todo_create"),
    path("get_all/", controller.get_all_todos, name="todo_get_all"),
    path("get/", controller.get_todo, name="todo_get"),
    path("update/", controller.update_todo, name="todo_update"),
    path("delete/", controller.delete_todo, name="todo_delete"),
]
