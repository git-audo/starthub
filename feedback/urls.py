from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_feedback, name='feedback'),
    path('new/', views.new_feedback, name='new-feedback'),    
]
