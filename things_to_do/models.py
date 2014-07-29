from django.db import models

# Create your models here.
class SelectedThingsToDoEntry(models.Model):
	category = models.CharField(max_length=30)
	latitude = models.DecimalField(max_digits=8, decimal_places=5)
	longitude = models.DecimalField(max_digits=8, decimal_places=5)
	description = models.CharField(max_length=200)
	hours = models.CharField(max_length=20)
	url = models.URLField()

class ThingsToDoEntry(models.Model):
	category = models.CharField(max_length=30)
	latitude = models.DecimalField(max_digits=8, decimal_places=5)
	longitude = models.DecimalField(max_digits=8, decimal_places=5)
	description = models.CharField(max_length=200)
	hours = models.CharField(max_length=20)
	url = models.URLField()
