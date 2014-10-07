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
        """
        Should return a url that looks like /guestbook/<created_by>/<pk>/
        """
        return reverse('guestbook-detail',
                kwargs={
                    'pk': self.pk,
                    'created_by': self.created_by,
                    }
                )

    def get_absolute_update_url(self):
        """
        Should return a url that looks like /guestbook/<created_by>/<pk>/update/
        """
        return reverse('guestbook-update',
                kwargs={
                    'pk': self.pk,
                    'created_by': self.created_by,
                    }
                )

    def get_absolute_delete_url(self):
        """
        Should return a url that looks like /guestbook/<created_by>/<pk>/delete/
        Not sure if I need this url, it will probably redirect to something else.
        """
        return reverse('guestbook-delete',
                kwargs={
                    'pk': self.pk,
                    'created_by': self.created_by,
                    }
                )
