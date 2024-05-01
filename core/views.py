from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, DetailView, CreateView


class Menu(TemplateView):
    template_name = "menu.html"


class Update(UpdateView):
    template_name = "update.html"


class Delete(DetailView):
    template_name = "delete.html"


class Create(CreateView):
    template_name = "create.html"
