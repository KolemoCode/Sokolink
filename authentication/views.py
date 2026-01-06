from django.shortcuts import render,redirect
from . forms import UserForm,LoginForm
from django.contrib.auth import authenticate, login,logout

def signup(request):
    if request.method =='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user =form.save()
            login(request,user)
            return redirect('products')
    else:
        form = UserForm()

    return render(request, "signup.html",{"form":form})


def login_view(request):
    if request.method == 'POST':
         form = LoginForm(request,data=request.POST)
         if form.is_valid():
                user = form.get_user()
                login(request,user)
                return redirect('products')
    else:
        form = LoginForm()

    return render(request,'login.html',{"form":form})



def logout(request):
    logout(request)
    return redirect('signup.html')


