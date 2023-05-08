from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from ros.models import Creature, Spell, Skill, Character
from ros.owner import OwnerListView, OwnerDetailView
#from autos.forms import MakeForm

# Create your views here.


class CreatureListView(OwnerListView):
    model = Creature


class SpellListView(OwnerListView):
    model = Spell


class SkillListView(OwnerListView):
    model = Skill


class CharacterListView(OwnerListView):
    model = Character


class CreatureDetailView(OwnerDetailView):
    model = Creature
    template_name = "ros/creature_detail.html"
    def get(self, request, pk) :
        x = Creature.objects.get(id=pk)
        context = {'creature': x}
        return render(request, self.template_name, context)

class SpellDetailView(OwnerDetailView):
    model = Spell
    template_name = "ros/spell_detail.html"
    def get(self, request, pk) :
        x = Spell.objects.get(id=pk)
        context = {'spell': x}
        return render(request, self.template_name, context)

class SkillDetailView(OwnerDetailView):
    model = Skill
    template_name = "ros/skill_detail.html"
    def get(self, request, pk) :
        x = Skill.objects.get(id=pk)
        context = {'skill': x}
        return render(request, self.template_name, context)

class CharacterDetailView(OwnerDetailView):
    model = Character
    template_name = "ros/character_detail.html"
    def get(self, request, pk) :
        x = Character.objects.get(id=pk)
        context = {'character': x}
        return render(request, self.template_name, context)



