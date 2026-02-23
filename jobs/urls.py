from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.jobs_listing, name='jobs'),
    path("job/<int:id>/", views.job_details, name="job_details"),
    path('add_job/',views.add_job,name='add_job'),

]