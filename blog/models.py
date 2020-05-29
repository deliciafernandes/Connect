from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#reverse function
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100) #restricted
	content = models.TextField() #unrestricted
	date_posted = models.DateTimeField(default = timezone.now) 
	#no parenthesis timezon.now() eventhough timezone.now is funtion because 
	# we dont want to execute the function, 
	# we want to give the whole function as an argument
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	#on_delete used to tell django what to do incase of deletion of the user
	#Eg. If on instagram a user deletes their account,
	#Even their pics get deletd, same way if a user gets deleted here
	# we should delete their posts too
	#Note: If a post gets deleted, user still exists

	#One to Many relation:
	#One User can have many posts
	#One posts can have only one user

	def __str__(self):
		return self.title

	def  get_absolute_url(self):
		#will return the full path to the route
		#needs a specific post with the primary key
		#instance of a specific post = primary key
		return reverse('post-detail', kwargs={'pk':self.pk})