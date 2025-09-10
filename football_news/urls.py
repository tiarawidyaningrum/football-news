from django.contrib import admin
from django.urls import path, include  # <- tambah include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # <- tambah baris ini
]