from django.urls import path

from . import views

urlpatterns = [
    #path ('', views.MainView.as_view(), name='all'),
    path('creatures', views.CreatureListView.as_view(), name='creatures'),
    #path('creatures/<int:pk>', views.CreatureDetailView.as_view(), name='creature_detail'),
    path('spells', views.SpellListView.as_view(), name='spells'),
    path('skills', views.SkillListView.as_view(), name='skills'),
]