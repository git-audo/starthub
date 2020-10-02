from django import forms
from board.models import Post
from django.contrib.postgres.forms import SimpleArrayField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'tag']
        
    
