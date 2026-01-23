from django.db import models
from django. contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    pass

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    username_or_businessname = models.CharField(max_length=100,blank=True)
    profile_pic =models.ImageField(upload_to='images/',default=None) 
    location = models.CharField(max_length=100,blank=True)
    phone_number = PhoneNumberField(max_length=50,blank=True)

