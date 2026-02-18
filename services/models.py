from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "services")
    category = models.ForeignKey(ServiceCategory,on_delete=models.SET_NULL,null=True)
    service = models.CharField(max_length=100,blank=True)
    charging_rate = models.DecimalField(max_digits=50,decimal_places=2)
    
    def __str__(self):
        return f" {self.user.username}"
