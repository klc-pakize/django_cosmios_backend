from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    number = models.PositiveSmallIntegerField(null=True, blank=True)
    about = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    register_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_actite = models.BooleanField(default=True)
    avatar = models.ImageField(blank=True, null=True, upload_to="student")
    age = models.PositiveBigIntegerField()
    
    class Meta:
        ordering = ["-number"]
        verbose_name = "ÖĞRENCİLER"
        verbose_name_plural = "ÖĞRENCİLER_LİSTESİ"

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.number}"