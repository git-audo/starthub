from django.forms import ModelForm
from board.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'tag']
    
