from django.shortcuts import render
from django.views import generic
from board.models import Post
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView

from .forms import PostForm

class PostsListView(generic.ListView):
    model = Post
    template_name = 'index.html'

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    
    
def index(request):
    context['posts']
    for post in Post.objects.all():
        context += post

        
    return render(request, 'index.html', context=context)


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    return render(request, 'form.html', {'form': form})
