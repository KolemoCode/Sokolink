from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.service_list, name='services'),
    path("service/<int:id>/", views.service_details, name="service_details"),
    path('add_service/',views.add_service,name='add_service'),
    
]