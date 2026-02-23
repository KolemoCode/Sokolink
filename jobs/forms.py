from . models import Job
from django import forms

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['user']