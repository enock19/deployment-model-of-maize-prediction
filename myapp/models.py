from typing import Any
from django.db import models


# Load the ML model outside the model class for efficiency (one-time load)


class Data(models.Model):
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()
    prediction = models.PositiveIntegerField(null=True,blank=True)

  

  


