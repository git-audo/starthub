from django import forms
from board.models import Post
from django.contrib.postgres.forms import SimpleArrayField


class SignupForm(forms.Form):
    username = forms.CharField()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'detailed_description', 'tags']

        
    
