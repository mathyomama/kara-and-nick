from django.db import models

# Create your models here.
class GalleryEntry(models.Model):
	image = models.ImageField()
	description = models.CharField(max_length=200)
	tag = models.CharField(max_length=30)

class GalleryUploadEntry(models.Model):
	image = models.ImageField()
	#account = models.ForeignKey('rsvp.Account')
	person = models.ForeignKey('rsvp.Person')
	date_added = models.DateField(auto_now_add=True)
