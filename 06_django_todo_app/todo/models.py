from django.db import models

# Create your models here.

class Todo(models.Model):

    PRIORIY = (
        (1, 'High'),  # db, kullanıcı
        (2, 'Medium'),
        (3, 'Low'),
    )

    task = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    priority = models.PositiveSmallIntegerField(choices=PRIORIY, default=3)
    is_done = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task} - {self.priority}"