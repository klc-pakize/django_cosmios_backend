from django.urls import path, include

from rest_framework import routers

from .views import FlightMVS, ReservationMVS

router = routers.DefaultRouter()
router.register("flight", FlightMVS)  # flight  flight/id
router.register("reservation", ReservationMVS)  # reservation  reservation/id


urlpatterns = [
    path("", include(router.urls))
]
