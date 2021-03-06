from django import forms
from models import Message, Category, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class MessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'save'))
        self.helper.form_class = 'form-horizontal'

        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'

    class Meta:
        model = Message
        exclude = ('related_user', 'related_event', 'related_message')
        fields = ('title', 'body', 'file', 'related_categories')


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper= FormHelper(self)
        self.helper.layout.append(Submit('save', 'Comment'))
        self.helper.form_class = "form-horizontal"

        self.helper.label_class = 'hidden'
        self.helper.field_class = 'col-sm-12'

    class Meta:
        model = Comment
        exclude = ("related_user", "related_message")
