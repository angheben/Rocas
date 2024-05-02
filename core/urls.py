from django.urls import path
from .views import MenuView, CreatePostView, DeleteView, UpdateView, LogoutView, LoginView, SignUpView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", MenuView.as_view(template_name="menu.html"), name="menu"),
    path("post/update/<int:pk>", MenuView.as_view(template_name="update.html"), name="update"),
    path("post/delete/<int:pk>", MenuView.as_view(template_name="delete.html"), name="delete"),
    path("post", CreatePostView.as_view(template_name="post.html"), name="post"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("signup/", SignUpView.as_view(template_name="signup.html"), name="signup"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
