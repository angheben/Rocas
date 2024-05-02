from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, DetailView, CreateView, RedirectView
from .models import Post
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.forms import UserCreationForm


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


class LogoutView(RedirectView):
    url = reverse_lazy('menu')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class LoginView(BaseLoginView):
    template_name = "login"


class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

