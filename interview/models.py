from operator import mod
from zoneinfo import available_timezones
from django.db import models

# Create your models here.

class shedule(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    starttime = models.IntegerField()
    endtime = models.IntegerField()
    is_candidates = models.BooleanField(default=True)