from django.db.models.signals import post_save
#this is an import that gets fired an object is saved
#so we want to give the signal when a user is created, import user
from django.contrib.auth.models import User
#sender - User model
#this is going to send a signal that the user is created
from django.dispatch import receiver
#receiver 

#import Profile from models, since we want a profile for user to be created on registration
from .models import Profile

#tie it all together use decorator
#@receiver( signal that we want, sender )

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
		#user is instance seeeeeeee |up|

#**kwargs: accepts any additional keyword arguments onto the end of the function

@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

