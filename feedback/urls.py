from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_feedback, name='feedback'),
]
