from django.db import models

# Create your models here.


class Task(models.Model):
    description = models.CharField(max_length=150, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.description
