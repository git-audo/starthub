from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from .forms import SignupForm, PostForm
from board.models import Post
import datetime


def index(request):
    context['posts']
    for post in Post.objects.all():
        context += post
        
    return render(request, 'index.html', context=context)


def login(request):
    return render(request, 'signup.html')


def signup(request):
    if request.method == 'POST':
        return
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


@csrf_exempt
def new_post(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            post = Post()
            post.title = request.POST.get('title')
            post.description = request.POST.get('description')            
            post.detailed_description = request.POST.get('detailed_description')
            post.tags = request.POST.getlist('tags')[0].split(' ')
            post.author = request.user.get_full_name().split(" ")[0]
            post.publication_date = datetime.date.today()
            post.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/board/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    return render(request, 'form.html', {'form': form})


class PostsListView(generic.ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post.html'
