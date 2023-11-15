from django.urls import path, include

from .views import RegisterAPIView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path("register/", RegisterAPIView.as_view()),
]
