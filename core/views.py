from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView, RedirectView, FormView
from .models import Post
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User


class MenuView(TemplateView):
    """
    This class will serve to display the menu page of the application
    """
    template_name = "menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve all posts ordered by creation date
        posts = Post.objects.all().order_by('-created_on')
        context['posts'] = posts
        return context


class UpdatePostView(UpdateView):
    """
    This class will serve users to update information in their posts
    """
    template_name = "update.html"
    model = Post
    fields = ['image', 'title', 'content']


class DeletePostView(DeleteView):
    """
    This class will serve to delete posts and redirect users to the menu
    """
    template_name = "delete.html"
    model = Post
    url = reverse_lazy("menu")


class CreatePostView(CreateView):
    """
    This class will serve users to create new posts
    """
    template_name = "create.html"
    models = Post


class LogoutView(RedirectView):
    """
    This class serves to users logout of the blog and redirect to the menu page
    """
    url = reverse_lazy('menu')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class LoginView(FormView):
    """
    This class serves to manage the login page
    """
    template_name = "login"
    form_class = LoginForm
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        """
        This function is called when the user do the login correctly
        """
        messages.success(self.request, message="Login successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        This function is called when the user do the login incorrectly
        """
        messages.error(self.request, message="Invalid username or password")
        return super().form_invalid(form)


class SignUpView(FormView):
    """
    This class serves to manage the signup page
    """
    template_name = "signup.html"
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """
        This function is called when the user do the login correctly
        """

        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        User.objects.create_user(username=username, email=email, password=password, is_active=True)

        messages.success(self.request, message="Login successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        This function is called when the user do the login incorrectly
        """
        messages.error(self.request, message="Invalid information")
        return super().form_invalid(form)

