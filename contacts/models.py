from django.db import models
from localflavor.us.models import PhoneNumberField

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=30)
	phone = PhoneNumberField()
	email = models.EmailField()

	def __unicode__(self):
		return self.name
