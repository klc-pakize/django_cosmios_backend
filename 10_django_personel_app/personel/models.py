from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Department model
class Department(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


# Personnel model
class Personnel(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    # choices for title
    TITLE_CHOICES = (
        ("1",  "Team Lead"),
        ("2", "Mid Lead"),
        ("3", "Junior")
    )

    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    
    # choices for gender
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female")
    )

    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    salary = models.PositiveIntegerField(null=True)
    # date_time_field shall be updated when new personnel is registered
    start_date = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.title} - {self.department}"