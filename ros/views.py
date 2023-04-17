from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ros.models import Creature

from ros.models import Creature
from ros.owner import OwnerListView, OwnerDetailView
#from autos.forms import MakeForm

# Create your views here.


class CreatureListView(OwnerListView):
    model = Creature
    # By convention:
    # template_name = "myarts/article_list.html"
