from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from . forms import ServiceForm
from .models import Service

# Create your views here.

def service_list(request):
    services = Service.objects.all()   # 👈 fetch from DB
    return render(request, 'services.html',{"services":services})

def service_details(request,id):
    service = get_object_or_404(Service, id=id)
    return render(request, "service_details.html", {"service": service})

def add_service(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)

        if form.is_valid():
            service = form.save(commit=False)
            service.user = request.user
            service.save()
            return redirect("service_details", id=service.id)
    else:
        form = ServiceForm()
    return render(request,'add_service.html',{"form":form})