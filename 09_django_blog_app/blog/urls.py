from django.urls import path, include

from rest_framework import routers

from .views import CategoryMVS, BlogMVS

router = routers.DefaultRouter()
router.register("category", CategoryMVS)  #  category/   category/<int:pk>/
router.register("blog", BlogMVS)  #  blog/   blog/<int:pk>/

urlpatterns = [
    # path("", include(router.urls))
] + router.urls