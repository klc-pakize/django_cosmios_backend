from django.db import models

class Path(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

class Student(models.Model):
    path = models.ForeignKey(Path, on_delete=models.SET_NULL, null=True, related_name="students")
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    number = models.PositiveSmallIntegerField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

