from django.urls import path
from .views import Menu, Create, Delete, Update


urlpatterns = [
    path("", Menu.as_view(), name="menu.html")
]
