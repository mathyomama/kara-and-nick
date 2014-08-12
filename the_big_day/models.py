from django.db import models
from localflavor.us.models import PhoneNumberField

# Create your models here.
class ItineraryEntry(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image_desciptive = models.ImageField()
    time = models.DateTimeField()
    phone = PhoneNumberField()
    image_location_1 = models.ImageField()
    string_location_1 = models.CharField(max_length=100)
    image_location_2 = models.ImageField()
    string_location_2 = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

class WhatToExpect(models.Model):
    mens_attire = models.CharField(max_length=200)
    womens_attire = models.CharField(max_length=200)
    seating_arrangement = models.URLField()
    menu = models.URLField()
