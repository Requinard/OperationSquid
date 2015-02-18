from django import forms
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

class LoginForm(forms.Form):
    username = forms.CharField(
        label = "Username",
        max_length=20,
        required=True,
    )

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Log in'))
        super(LoginForm, self).__init__(*args, **kwargs)