from django.db import models

# Create your models here.
class OurStoryEntry(models.Model):
	title = models.CharField(max_length=100)
	transcript = models.TextField()
	image_thumbnail = models.ImageField()
	video = models.FileField()

	def __unicode__(self):
		return title
