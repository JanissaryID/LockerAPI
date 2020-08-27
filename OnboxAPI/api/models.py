from django.db import models

# Create your models here.

class Lockers(models.Model):
    IdLocker = models.CharField(max_length=15)
    QuantityBox = models.PositiveIntegerField()

    def __str__(self):
        return self.IdLocker

    class Meta:
        ordering = ['IdLocker']

class Boxs(models.Model):
    NumberBox = models.PositiveIntegerField()
    Password = models.CharField(max_length=50)
    OnRent = models.BooleanField(default=False)
    DoorBox = models.BooleanField(default=False)
    IdLocker = models.ForeignKey(Lockers, related_name='boxs', on_delete=models.CASCADE)

    class Meta:
        ordering = ['NumberBox']