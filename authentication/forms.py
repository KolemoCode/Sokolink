from django import forms
from .models import User,Profile
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email")

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','username_or_businessname','location','phone_number']  # ImageField
        widgets = {
            'profile_pic': forms.ClearableFileInput(attrs={
                'class': 'inputfile',  # we'll style it manually
                'id': 'id_profile_pic'
            })
        }
