from django import forms
from .models import GuestbookEntry
from django.utils.translation import ugettext_lazy as _
from rsvp.models import Account, Person

class GuestbookEntryForm(forms.ModelForm):
    class Meta:
        model = GuestbookEntry
        exclude = ['created_by', 'date']
        labels = {
                'name': _('From'),
                }
