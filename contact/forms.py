from django.forms import ModelForm
from .models import ContactModel


class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'e_mail', 'message']
        labels = {
            'name': 'Name:',
            'e_mail': 'E-mail:',
            'message': 'Message:'
        }
