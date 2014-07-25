from django.db import models

# Create your models here.
class AccommodationsEntry(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	image1 = models.ImageField()
	image2 = models.ImageField()
	image3 = models.ImageField()
	url = models.URLField()

	def __unicode__(self):
		return self.name
