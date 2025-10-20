from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name