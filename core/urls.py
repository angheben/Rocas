from django.urls import path
from .views import MenuView, CreateView, DeleteView, UpdateView, LogoutView, LoginView, SignUpView


urlpatterns = [
    path("", MenuView.as_view(template_name="menu.html"), name="menu"),
    path("post/update/<int:pk>", MenuView.as_view(template_name="update.html"), name="update"),
    path("post/delete/<int:pk>", MenuView.as_view(template_name="delete.html"), name="delete"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("signup/", SignUpView.as_view(template_name="signup.html"), name="signup"),
]
