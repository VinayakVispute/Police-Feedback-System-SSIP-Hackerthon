from django.db import models
from django.utils import timezone
# Create your models here.

class displayReport(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    police_station = models.CharField(max_length=50)
    how_come = models.CharField(max_length=50)
    time_taken = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    feedback = models.TextField()
    rating = models.PositiveSmallIntegerField()
    date = models.DateField(default=timezone.now)

class stateWisePoliceStation(models.Model):
    state = models.CharField(max_length=15)
    police_station= models.CharField(max_length=15)
    qr_code = models.FileField(upload_to="qrCodes/", max_length=250, null=True, default=None)
    





