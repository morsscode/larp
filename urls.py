from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ros/', include('ros.urls')),
    path('admin/', admin.site.urls),
]