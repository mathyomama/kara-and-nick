from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class GuestbookEntry(models.Model):
    account = models.ForeignKey(User, unique=True)
    name = models.CharField(max_length=50)
    person = models.ForeignKey('rsvp.Person')
    location = models.CharField(max_length=100)
    note = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name
