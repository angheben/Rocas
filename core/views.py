from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, DetailView, CreateView
from .models import Post


class Menu(TemplateView):
    template_name = "menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve all posts ordered by creation date
        posts = Post.objects.all().order_by('-created_on')
        context['posts'] = posts
        return context


class Update(UpdateView):
    template_name = "update.html"
    model = Post
    fields = ['image', 'title', 'content']


class Delete(DetailView):
    template_name = "delete.html"
    model = Post


class Create(CreateView):
    template_name = "create.html"
    models = Post

