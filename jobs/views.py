from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from . forms import JobForm
from .models import Job

# Create your views here.

def jobs_listing(request):
    jobs = Job.objects.all()   # 👈 fetch from DB
    return render(request, 'jobs_listing.html',{"jobs":jobs})

def job_details(request,id):
    job = get_object_or_404(Job, id=id)
    return render(request, "job_details.html", {"job": job})

def add_job(request):
    if request.method == "POST":
        form = JobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect("job_details", id=job.id)
    else:
        form = JobForm()
    return render(request,'add_job.html',{"form":form})
