from django import forms
from .models import GuestbookEntry
from django.utils.translation import ugettext_lazy as _
from rsvp.models import Account, Person

class GuestbookEntryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """
        The __init__ method is modified to accept another keyword argument which will be the queryset of
        people associated with the account, i.e. the people who are rsvped for that acccount.
        """
        people = kwargs.pop('people')
        super(GuestbookEntryForm, self).__init__(*args, **kwargs)
        self.fields['person'] = forms.ModelChoiceField(
                queryset=people,
                empty_label=_('Guest'),
                to_field_name='person',
                label=_('From'),
                )

    class Meta:
        model = GuestbookEntry
        exclude = ['created_by', 'date']
