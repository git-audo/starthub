from django import forms
from feedback.models import Feedback
from django.contrib.postgres.forms import SimpleArrayField


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['description', 'contact']
        labels = {
            'description': 'Descrizione',
            'contact': 'Email'
        }
