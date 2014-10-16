from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import re

# Create your models here.
class GuestbookEntry(models.Model):
    created_by = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    note = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % self.name
    
    def get_absolute_url(self):
        """
        Should return a url that looks like /guestbook/entry/<pk>/
        """
        return reverse('guestbook-detail',
                kwargs={
                    'pk': self.pk,
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
    def get_html_id(self):
        return "%s-%s" % (removeBadChar(self.name), self.pk)

def removeBadChar(string):
    return re.sub(r'\W', '', string)
