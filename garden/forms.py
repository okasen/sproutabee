from .models import Garden
from django import forms
from accounts.models import User
from django.utils.translation import ugettext_lazy as _


class CreateGardenForm(forms.ModelForm):
    class Meta:
        model = Garden
        fields = ('name', 'length', 'width', 'type')
        labels = {
            'name': _('Your plot name'),
            'length': _('Plot length in meters'),
            'width': _('Plot width in meters'),
        }
        error_messages = {
            'name': {
                'max_length': _("This plot name is too long."),
            },
        }
    def __init__(self, *args, **kwargs):
        super(CreateGardenForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'namefield'})
        self.fields['length'].widget.attrs.update({'class' : 'lengthfield'})
        self.fields['width'].widget.attrs.update({'class' : 'widthfield'})
        self.fields['type'].widget.attrs.update({'class' : 'typefield'})
