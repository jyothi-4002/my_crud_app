from django.urls import path
from core_app.todo import controller  # <-- import controller instead of views

urlpatterns = [
    path("create/", controller.create_todo, name="todo_create"),
    path("get_all/", controller.get_all_todos, name="todo_get_all"),
    path("get/<int:todo_id>/", controller.get_todo, name="todo_get"),
    path("update/<int:todo_id>/", controller.update_todo, name="todo_update"),
    path("delete/<int:todo_id>/", controller.delete_todo, name="todo_delete"),
]
