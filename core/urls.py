from django.urls import path
from .views import Menu, Create, Delete, Update


urlpatterns = [
    path("", Menu.as_view(template_name="menu.html"), name="menu"),
    path("post/update/<int:pk>", Menu.as_view(template_name="update.html"), name="update"),
    path("post/delete/<int:pk>", Menu.as_view(template_name="delete.html"), name="delete"),
]
