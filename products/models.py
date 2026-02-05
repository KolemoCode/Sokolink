from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name = "Product")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name = "products",null=True,blank=True)
    product_name = models.CharField(max_length=80, blank=True)
    product_img = models.ImageField(upload_to='product/',default=None)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available = models.BooleanField(default=True)
    negotiable = models.BooleanField(default=False)
    time_posted = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.title

