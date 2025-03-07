from django import forms
from django.core.exceptions import ValidationError
from . import models




class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone',)

    def clean(self):
        self.add_error('first_name',ValidationError('Mensagem', code='invalid'))
        return super().clean()