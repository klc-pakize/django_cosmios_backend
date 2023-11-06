from django.urls import path, include

from .views import DepartmanListCreateAPIView, PersonnelListCreateAPIView, DepartmentPersonnelView, PersonnelRetrieveUpdateDestroyAPIView


urlpatterns = [
    path("departman/", DepartmanListCreateAPIView.as_view()),
    path("departman/<str:department>/", DepartmentPersonnelView.as_view()),
    path("personnel/", PersonnelListCreateAPIView.as_view()),
    path("personnel/<int:pk>/", PersonnelRetrieveUpdateDestroyAPIView.as_view()),
]