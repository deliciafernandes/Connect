from django.shortcuts import render, get_object_or_404
from .models import Post
#. since models is in same directory 

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#for the UserListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
	context={
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

#to see difference
class PostListView(ListView):

	#we need to create a variable called model
	#this will tell the list which model to query inorder to create the list
	model = Post
	#next tell the blog/urls.py module to use this class inside of above function
	
	template_name = 'blog/home.html'
	#<app>/<model>_<viewtype>.html 

	#Now in our home view, we called all our post objects as posts in our context
	#but our PostListView calls all our lists items/ posts as object lists
	#now either we can change it in our template and tell it to use object list
	#or we either change the variable name to post
	context_object_name = 'posts'

	#inorder to change the post listing order
	ordering = ['-date_posted']
	#'date_posted' oldest to newest
	#'-date_posted' newest to oldest

	paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    #ordering = ['-date_posted']  does ordering down in get_queryset function
    paginate_by = 5

    #override method to get user specific posts
    def get_queryset(self):
    	#the specific user
		#if user doesn't exist return 404
		#use shortcut
		#if user exists, user variable gets user
		#else user variable returns 404 error
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

#this will be a view for individual posts uses detail view
class PostDetailView(DetailView):
	model = Post

#this will be a view for creating new post
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']
	#date_posted will be automatic

	#Overriding form.valid()
	def form_valid(self, form):
		form.instance.author = self.request.user


		#now this return will run our parent class form_valid() again but now before running it
		#we are overriding the author details
		return super().form_valid(form)

#exactly same as PostCreateView
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']
	def form_valid(self, form):
		form.instance.author = self.request.user

		return super().form_valid(form)

	def test_func(self):
		#we need to get the exact post that we are currently updating
		#the way that we can do this is using a method of the update view called as get_object
		post = self.get_object() #now we'll get the post that we're currently trying to update
		
		#check to make usre that the current user is the author of the post
		if self.request.user == post.author:
			#current logged in user = self.request.user
			#allow
			return True
		else:
			return False

#Similar to detail view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post

	success_url = '/'
	
	def test_func(self):
		#we need to get the exact post that we are currently updating
		#the way that we can do this is using a method of the update view called as get_object
		post = self.get_object() #now we'll get the post that we're currently trying to update
		
		#check to make usre that the current user is the author of the post
		if self.request.user == post.author:
			#current logged in user = self.request.user
			#allow
			return True
		else:
			return False

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'} )
