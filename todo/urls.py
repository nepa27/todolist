"""URLs for todo project."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('list_todo.urls')),
    path('', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]
