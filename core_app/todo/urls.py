# core_app/todo/urls.py
from django.urls import path
from core_app.todo import views

urlpatterns = [
    path("create/", views.create, name='todo-create'),
    path("get_all/", views.get_all, name='todo-get-all'),
    path("get/<int:todo_id>/", views.get, name='todo-get'),
    path("update/<int:todo_id>/", views.update, name='todo-update'),
    path("delete/<int:todo_id>/", views.delete, name='todo-delete'),
]
