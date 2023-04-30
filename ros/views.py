from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from ros.models import Creature, Spell, Skill
from ros.owner import OwnerListView, OwnerDetailView
#from autos.forms import MakeForm

# Create your views here.


class CreatureListView(OwnerListView):
    model = Creature
    # By convention:
    # template_name = "ros/creature_list.html"


class CreatureDetailView(OwnerDetailView):
    model = Creature
    template_name = "ros/creature_detail.html"
    def get(self, request, pk) :
        x = Creature.objects.get(id=pk)
        #comments = Comment.objects.filter(ad=x).order_by('-updated_at')
        #comment_form = CommentForm()
        context = {'creature': x}  #'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)

class SpellDetailView(OwnerDetailView):
    model = Spell
    template_name = "ros/spell_detail.html"
    def get(self, request, pk) :
        x = Spell.objects.get(id=pk)
        #comments = Comment.objects.filter(ad=x).order_by('-updated_at')
        #comment_form = CommentForm()
        context = {'spell': x}  #'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)

class SkillDetailView(OwnerDetailView):
    model = Skill
    template_name = "ros/skill_detail.html"
    def get(self, request, pk) :
        x = Skill.objects.get(id=pk)
        #comments = Comment.objects.filter(ad=x).order_by('-updated_at')
        #comment_form = CommentForm()
        context = {'skill': x}  #'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)



class SpellListView(OwnerListView):
    model = Spell


class SkillListView(OwnerListView):
    model = Skill