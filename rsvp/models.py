from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
	user = models.OneToOneField(User)
	reservations = models.PositiveIntegerField()

	def __unicode__(self):
		return self.user.get_username()

class Person(models.Model):
	account = models.ForeignKey(Account)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.EmailField()
	medical_issues = models.CharField(max_length=200)
	updates = models.BooleanField(default=False)

	def __unicode__(self):
		return ' '.join((self.first_name, self.last_name))
