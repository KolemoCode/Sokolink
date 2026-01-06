from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def messages(request):
    return render(request, 'chat.html')
