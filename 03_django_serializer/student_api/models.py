from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    number = models.PositiveSmallIntegerField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"