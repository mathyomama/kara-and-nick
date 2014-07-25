from django.db import models

# Create your models here.
class GuestbookEntry(models.Model):
	account = models.ForeignKey('rsvp.Account')
	name = models.CharField(max_length=50)
	#person = models.ForeignKey('rsvp.Person')
	location = models.CharField(max_length=100)
	note = models.TextField()
	date = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.name
