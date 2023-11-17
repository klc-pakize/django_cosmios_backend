from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Flight Table
class Flight(models.Model):
    # each passenger should have a flight number
    flight_number = models.CharField(max_length=4, unique=True)
    # airline information should be entered. Flight numbers are used to identify different flights operated by different airlines.
    operating_airlines = models.CharField(max_length=50)
    # departure city should be entered. The departure city is usually included in the tickets.
    departure_city = models.CharField(max_length=85) 
    # arrival city should be entered. The arrival city is usually included in the tickets.
    arrival_city = models.CharField(max_length=85)
    # auto_now shall be used. The date is automatically updated when any updates are made.
    date_of_departure = models.DateField()
    # auto_now shall be used. The time is automatically updated when any updates are made.
    estimated_time_of_departure = models.TimeField()

    def __str__(self):
        return f"{self.flight_number} - {self.operating_airlines} - {self.departure_city} - {self.arrival_city} - {self.date_of_departure} - {self.estimated_time_of_departure}"

# Passenger Table
class Passenger(models.Model):
    first_name = models.CharField(max_length=1019)  # the longest first name in the world is 1019 letters.
    last_name = models.CharField(max_length=666)  # the longest last name in the world is 666 letters.
    email = models.EmailField(max_length=345)  # the longest email in the world is 345 letters.
    # phone number consists of 10 characters. 
    phone_number = models.PositiveBigIntegerField()
    # auto_now shall be used. The date is automatically updated when any updates are made.
    update_date = models.DateField(auto_now=True)
    # auto_now add shall be used. The date is automatically updated when a new object is added.
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

# Reservation Table:
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    passenger = models.ManyToManyField(Passenger)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='flights')

    def __str__(self):
        return f"{self.flight}"