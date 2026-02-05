from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products, name='products'),
    path("add_product/", views.add_product, name="add_product"),
    path("<int:pk>/", views.product_detail, name="product_detail"),

]