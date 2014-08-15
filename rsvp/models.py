from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
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
    email = models.EmailField()
    medical_issues = models.CharField(max_length=200)
    updates = models.BooleanField(default=False)

    def __unicode__(self):
        return ' '.join((self.first_name, self.last_name))

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
