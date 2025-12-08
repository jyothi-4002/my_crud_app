from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core_app.urls')),            # hello/hai endpoints
    path('todo/', include('core_app.todo.urls')),  # TODO CRUD endpoints
]
