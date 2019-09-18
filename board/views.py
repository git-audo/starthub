from django.shortcuts import render
from django.views import generic
from board.models import Venture

class VentureListView(generic.ListView):
    model = Venture
    template_name = 'index.html'
    
def index(request):
    context['ventures']
    for venture in Venture.objects.all():
        context += venture

        
    return render(request, 'index.html', context=context)

