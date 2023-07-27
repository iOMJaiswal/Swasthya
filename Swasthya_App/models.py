from django.db import models
from datetime import datetime

class FirstAid(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

class Ambulance(models.Model):
    urgency = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    mobile = models.IntegerField()
    added_date = models.CharField(max_length=100, default=datetime.now())

class Patient(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    location = models.CharField(max_length=100)
    problem = models.CharField(max_length=100)
    booked_date = models.CharField(max_length=100, default=datetime.now())

