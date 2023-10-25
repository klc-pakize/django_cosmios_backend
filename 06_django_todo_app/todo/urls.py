from django.urls import path, include

from .views import home, todo_list_create, todo_detail, TodosListCreateAPIView, TodosDetailAPIView, TodoModelViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register("todos", TodoModelViewSet)  # todos/ todos/<int:pk>/

urlpatterns = [
    path("", home),
    # path("todos/", todo_list_create),
    # path("todo/<int:pk>/", todo_detail),

    # path("todos/", TodosListCreateAPIView.as_view()),
    # path("todos/<str:task>/", TodosDetailAPIView.as_view()),

    path("", include(router.urls)),
]
