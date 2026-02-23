from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Job(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "Job")
    job_title = models.CharField(max_length=100,blank=True)
    qualifications = models.CharField(max_length=1000)
    job_description = models.TextField(max_length=1000,blank=True)