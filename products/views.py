from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

# Product List View
def products(request):
    products = Product.objects.filter(available=True).order_by("time_posted")
    return render(request, "products_list.html", {"products": products})


# Product Detail View
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {"product": product})


# Product Create View
@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.location = product.user.profile.location  # from user profile
            product.save()
            return redirect("product_detail", pk=product.pk)
    else:
        form = ProductForm()

    return render(request, 'product_form.html', {"form": form})
