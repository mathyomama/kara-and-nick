from django.db import models

# Create your models here.
class OurStoryEntry(models.Model):
    question = models.CharField(max_length=100)
    transcript = models.TextField()
    image_thumbnail = models.ImageField()
    video = models.CharField(max_length=200)

    def __unicode__(self):
        return self.question 
