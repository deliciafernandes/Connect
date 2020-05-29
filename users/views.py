from django.shortcuts import render, redirect
#redirect imported to redirect user to homepage
from django.contrib import messages
#imported to use flash messages that will only be displayed once and disappeared the next second
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
#decorator for login_required


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		#creates a user form with this post data
		if form.is_valid():
			form.save()
			#if data is valid, get username
			username = form.cleaned_data.get('username')
			#this validated form data goes in the form.cleaned_data.get('username') dictionary
			#form.cleaned_data is a dict
			messages.success(request,f'{username} your account is now created! Please Log In') 
			return redirect('login')
			#blog-home = name of blog home url pattern
	else:
		form = UserRegisterForm()
	#instance of form created, = to classname(), here class is UserCreationForm
	return render(request, 'users/register.html', {'form': form})

	#Types of messages:
		# messages.debug
		# messages.info
		# messages.success
		# messages.warning
		# messages.error

#here, decorators add functionality to an existing function
@login_required
def profile(request):
	#if else case tp check if the form filled is a valid POST request or no
    if request.method == 'POST':
    	#this if case is true when submit button is clicked
 		#Create instance of UserUpdateForm and ProfileUpdateForm
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            #LETS GIVE THE USER A FEEDBACK THAT THE PROFILE IS UPDATED
            messages.success(request, f'Your account has been updated!')

            #NEXT REDIRECT THE USER TO THE PROFILE PAGE TO CHECK
            return redirect('profile')

    #IF NOT VALID, DON'T SAVE IT
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    #Next pass it to the template
    context = {
    	#keys
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)