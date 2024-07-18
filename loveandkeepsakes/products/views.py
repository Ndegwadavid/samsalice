from django.shortcuts import render
from management.models import Product, CATEGORY_CHOICES

def product_list(request):
    categories = dict(CATEGORY_CHOICES)
    return render(request, 'products/product_list.html', {'categories': categories})

def category_products(request, category):
    products = Product.objects.filter(category=category, in_stock=True)
    return render(request, 'products/category_products.html', {'products': products, 'category': category})