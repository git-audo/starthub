from django import forms
from board.models import Post
from django.contrib.postgres.forms import SimpleArrayField


class SignupForm(forms.Form):
    username = forms.CharField()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'detailed_description', 'tags', 'author', 'email']
        labels = {
            'title': 'Titolo',
            'description': 'Descrizione',
            'detailed_description': 'Descrizione completa',
            'tags': 'Tag',
            'author': 'Autore',
            'email': 'Email'
        }

    
