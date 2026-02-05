from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
        "category",  "description", "product_name","price",
        "product_img", "available", "negotiable"
        ]