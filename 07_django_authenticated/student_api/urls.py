from django.urls import path, include

from .views import (
    #! ViewSets
    StudentMVS,
    PathMVS
    )

from rest_framework import routers

#! ViewSets
router = routers.DefaultRouter()
router.register("studentmvs", StudentMVS)  # studentmvs/  studentmvs/<int:pk>/
router.register("path", PathMVS)

urlpatterns = [
    #! ViewSets
    # path("", include(router.urls)),
] + router.urls