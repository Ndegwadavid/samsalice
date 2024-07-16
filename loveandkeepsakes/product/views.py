from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})

def checkout(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product/checkout.html', {'product': product})