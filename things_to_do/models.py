from django.db import models

# Create your models here.
class SelectedThingsToDoEntry(models.Model):
	category = models.CharField(max_length=30)
	latitude = models.DecimalField()
	longitude = models.DecimalField()
	description = models.CharField(max_length=200)
	hours = models.CharField(max_length=20)
	url = models.URLField()

class ThingsToDoEntry(models.Model):
	category = models.CharField(max_length=30)
	latitude = models.DecimalField()
	longitude = models.DecimalField()
	description = models.CharField(max_length=200)
	hours = models.CharField(max_length=20)
	url = models.URLField()
