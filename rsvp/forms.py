from django.forms import ModelForm, Textarea
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext_lazy as _
from .models import Person

class PersonForm(ModelForm):
    
    def __init__(self, account, *args, **kwargs):
        self.account = account
        super(PersonForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        person = super(PersonForm, self).save(commit=False, *args, **kwargs)
        person.account = self.account
        person.save()
        return person

    class Meta:
        model = Person
        exclude = ['account']
        help_texts = {
                'dietary_concerns': _('Please list any food allergies or related concerns.'),
                'email': _('Giving your email is optional and will only be used to send out updates.'),
                'updates': _('Please check this box if you would like updates.'), # This field seems a little redundant since the act of giving an email would show that they are interested in updates.
                }
        widgets = {
                'dietary_concerns': Textarea(attrs={'col': 40, 'rows': 5}),
                }
