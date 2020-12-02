from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render
from feedback.models import Feedback
from .forms import FeedbackForm
import datetime


@csrf_exempt
def new_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            feedback = Feedback()
            feedback.description = request.POST.get('description')
            feedback.contact = request.POST.get('contact')            
            feedback.date = datetime.date.today()
            feedback.save()

            return HttpResponseRedirect('/board/')

    else:
        form = FeedbackForm()

    return render(request, 'form.html', {'form': form})

