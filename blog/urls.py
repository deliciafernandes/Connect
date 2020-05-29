from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

#direct import 

from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),

    #now to write the url pattern for PostDetailView we will have to be more specific
    #as in each post has to be called individually, so eg. post 1, post 2 ,post 3 ,etc.
    #so we will have to give a number varible to post 
    #thus path('route', view, name)
    #here the route will be a post/integer pointing to each primary key of the post
    #A primary key, also called a primary keyword, is a key in a relational database that is unique for each record. 
    #It is a unique identifier, such as a driver license number, telephone number (including area code), or vehicle identification number (VIN). 
    #A relational database must always have one and only one primary key.
    #here pk is a built-in detail view attribute, we can change it if we want in the class
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
   

    path('about/', views.about, name='blog-about')
]