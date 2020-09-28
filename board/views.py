from django.shortcuts import render
from django.views import generic
from board.models import Post

class PostsListView(generic.ListView):
    model = Post
    template_name = 'index.html'
    
def index(request):
    context['posts']
    for post in Post.objects.all():
        context += post

        
    return render(request, 'index.html', context=context)

