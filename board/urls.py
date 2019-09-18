from django.urls import path
from . import views

urlpatterns = [
    path('', views.VentureListView.as_view(), name='ventures'),
]
