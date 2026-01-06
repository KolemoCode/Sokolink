from django.db import models
from django. contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

    
class Profile(models.Model):
    username_or_businessname = models.CharField(max_length=100,blank=True)
    profile_pic =models.ImageField(upload_to='profileimg',default=None) 
    location = models.CharField(max_length=100,blank=True)
    phone_number = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.name
