from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, CATEGORY_CHOICES
from .forms import ProductForm
from django.contrib.auth import authenticate, login



def admin_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return function(request, *args, **kwargs)
        return redirect('management:login')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def login_view(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('management:dashboard')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('management:dashboard')
        else:
            return render(request, 'management/login.html', {'error': 'Invalid credentials or insufficient permissions'})
    return render(request, 'management/login.html')


@admin_required
def dashboard(request):
    categories = dict(CATEGORY_CHOICES)
    return render(request, 'management/dashboard.html', {'categories': categories})

@admin_required
def category_products(request, category):
    products = Product.objects.filter(category=category)
    category_name = dict(CATEGORY_CHOICES)[category]
    return render(request, 'management/category_products.html', {'category': category, 'category_name': category_name, 'products': products})

@admin_required
def add_product(request, category):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.category = category
            
            # Handle file upload
            if 'image' in request.FILES:
                product.image = request.FILES['image']
            
            product.save()
            return redirect('management:category_products', category=category)
    else:
        form = ProductForm(initial={'category': category})
    category_name = dict(CATEGORY_CHOICES)[category]
    return render(request, 'management/add_product.html', {'form': form, 'category': category, 'category_name': category_name})


@admin_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('management:category_products', category=product.category)
    else:
        form = ProductForm(instance=product)
    return render(request, 'management/edit_product.html', {'form': form, 'product': product})

@admin_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    category = product.category
    product.delete()
    return redirect('management:category_products', category=category)

@admin_required
def toggle_stock(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.in_stock = not product.in_stock
    product.save()
    return redirect('management:category_products', category=product.category)