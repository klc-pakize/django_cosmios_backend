from django.urls import path, include

from .views import home, home2

urlpatterns = [
  path("home/", home),
  path("cosmios/", home2),
]
