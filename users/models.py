from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	#this model needs to have a OneToOneField reLationship with the User
	#on delete argument
	#on deletion of profile, images, posts etc. of user gets deleted

	#you can add additional fields of bio or city etc.
	image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')

	#Create a dunder method for display
	def __str__(self):
		return f'{self.user.username} Profile'
		#Result eg. deliciafernandes Profile

	def save(self, ** kwargs):
		#this already exists in our parent Models class, but we're creating our own to add some functionalities to it

		#first run the save method of our parent class
		super().save()

		#now we're going to use Pillow to resize the image

		#to open the image, this will open our current image
		img = Image.open(self.image.path)

		#resizing to 300px
		if img.height>300 or img.width>300 :
			#resize
			output_size = (300, 300) #a tuple
			img.thumbnail(output_size) #this resizes it
			img.save(self.image.path)