from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostsListView.as_view(), name='posts'),
    path('signup/', views.signup, name='signup'),        
    path('post/new/', views.new_post, name='new-post'),
    path('post/get/<int:pk>', views.PostDetailView.as_view(), name='get-post'),    
]

