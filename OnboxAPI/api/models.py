from django.db import models

# Create your models here.

class Lockers(models.Model):
    IdLocker = models.CharField(max_length=15)
    QuantityBox = models.PositiveIntegerField()

    def __str__(self):
        return self.IdLocker