from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    bio = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='profile')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"
    

class Address(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} {self.name}"
    

class Product(models.Model):
    name = models.CharField(max_length=300)
    user = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.name}"