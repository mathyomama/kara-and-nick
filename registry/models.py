from django.db import models

# Create your models here.
class RegistryEntry(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    image = models.ImageField()
    url = models.URLField()

    def __unicode__(self):
        return self.name
