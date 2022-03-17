from django import forms
from django.forms import ModelForm

from .models import Mailing


class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = ('text', 'start_date', 'finish_date')
