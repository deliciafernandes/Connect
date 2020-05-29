from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	#inherits from UserCreationForm
	email = forms.EmailField()
	#required=fals
	#default required = true

	class Meta:
		#model that this form interacts with
		model = User
		#whenever this form validates, it creates a new User
		fields = ['username', 'email', 'password1', 'password2']
		#Nested namespace for the configurations and keeps the configurations in one place
		#Within the configs. we're saying that the model that will be affected will be the User model, its going to save it in the User model
		#the fileds that we have in this list is how we want the info to be saved as
		#This is now our completed 

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

#Now image is not update yet, because that is going to be in our Profile model not User model, see models.py
#User is a built in model from django.contrib.auth.models
#but Profile is created by use in models.
#this class update our image
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		#model that we want to work with is Profile
		fields = ['image']
		#fields that we want to work with are them

#now if we just leave till here, everything will look like one form
