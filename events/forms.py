from crispy_forms.helper import FormHelper
from django import forms
from crispy_forms.layout import Submit

from .models import Event


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.layout.append(Submit('save', 'save'))

        self.helper.form_class = 'form-horizontal'

        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'

    class Meta:
        model = Event
        exclude = ()