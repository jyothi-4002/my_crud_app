# core_app/todo/urls.py
from django.urls import path
from feature.todo.controller import TodoController

urlpatterns = [
    path("create/", TodoController.create, name="todo_create"),
    path("get_all/", TodoController.get_all, name="todo_get_all"),
    path("get/", TodoController.get, name="todo_get"),
    path("update/", TodoController.update, name="todo_update"),
    path("delete/", TodoController.delete, name="todo_delete"),
]
