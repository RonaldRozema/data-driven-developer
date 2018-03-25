from django.forms import ModelForm

from .models import ContactFormModel


class ContactForm(ModelForm):

    class Meta:
        model = ContactFormModel
        fields = ['subject', 'content', 'email', 'phone_number']