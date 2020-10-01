from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostsListView.as_view(), name='posts'),
    path('post/new/', views.get_name, name='new-post'),    
]

