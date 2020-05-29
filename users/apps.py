from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'

    #This ready method, imports our signals in the users app
    def ready(self):
    	import users.signals