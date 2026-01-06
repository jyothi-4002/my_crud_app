from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('music/', include('myapi.feature.music.urls')),
    path('todo/', include('myapi.feature.todo.urls')),
    path('artist/', include('myapi.feature.artist.urls')),  # ✅ must be included
]
