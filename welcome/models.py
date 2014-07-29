from django.db import models

# Create your models here.
class Welcome(models.Model):
	image = models.ImageField()
	description = models.TextField()
	welcome_font = models.CharField(max_length=30)
	signature_font = models.CharField(max_length=30)

class WelcomeUpdateEntry(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	date_added = models.DateField(auto_now_add=True)
