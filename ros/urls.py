from django.urls import path

from . import views

app_name = 'ros'
urlpatterns = [
    #path ('', views.MainView.as_view(), name='all'),
    path('creatures', views.CreatureListView.as_view(), name='creatures'),
    path('creatures/<int:pk>', views.CreatureDetailView.as_view(), name='creature_detail'),
    path('spells', views.SpellListView.as_view(), name='spells'),
    path('spells/<int:pk>', views.SpellDetailView.as_view(), name='spell_detail'),
    path('skills', views.SkillListView.as_view(), name='skills'),
    path('skills/<int:pk>', views.SkillDetailView.as_view(), name='skill_detail'),
    path('characters', views.CharacterListView.as_view(), name='characters'),
    path('characters/<int:pk>', views.CharacterDetailView.as_view(), name='character_detail'),
]