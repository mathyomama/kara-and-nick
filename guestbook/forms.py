from django.forms import ModelForm
from .models import GuestbookEntry

class GuestbookEntryForm(ModelForm):

    class Meta:
        model = GuestbookEntry
        exclude = ['account']
