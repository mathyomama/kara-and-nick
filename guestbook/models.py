from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class GuestbookEntry(models.Model):
    created_by = models.ForeignKey(User, null=True)
    #name = models.CharField(max_length=50)
    person = models.OneToOneField('rsvp.Person', unique=True, null=True)
    location = models.CharField(max_length=100)
    note = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % self.person
    
    def get_absolute_url(self):
        #return "/guestbook/%s/%s/" % (self.created_by.get_username(), self.pk)
        return reverse('guestbook-detail',
                kwargs={
                    'pk': self.pk,
                    'created_by': self.created_by,
                    }
                )
