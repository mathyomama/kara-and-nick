from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.core.urlresolvers import reverse
from .signals import create_user_groups, put_account_into_guest
import sys

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
    dietary_concerns = models.TextField(max_length=500, blank=True)
    email = models.EmailField(blank=True)
    updates = models.BooleanField(default=False)

    def get_html_id(self):
        return "%s-%s-%s" % (self.first_name, self.last_name, self.pk)

    def get_absolute_update_url(self):
        return reverse(
                'rsvp-update',
                kwargs={
                    'pk': self.pk,
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    },
                )
    
    def get_absolute_delete_url(self):
        return reverse(
                'rsvp-delete',
                kwargs={
                    'pk': self.pk,
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    },
                )

    def __unicode__(self):
        return ' '.join((self.first_name, self.last_name))

class Image(models.Model):
    rsvp_image = models.ImageField()

# Creating the signal for installing groups
signals.post_syncdb.connect(
        create_user_groups,
        sender=sys.modules[__name__],
        dispatch_uid='rsvp.signals.create_user_groups'
        )

# Creating the signal for adding accounts into 'Guest'
signals.post_save.connect(
        put_account_into_guest,
        sender=Account,
        dispatch_uid='rsvp.signals.put_account_into_guest'
        )
