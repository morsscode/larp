from django.urls import path

from . import views

urlpatterns = [
    path('', views.CreatureListView.as_view(), name='all'),
]