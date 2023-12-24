from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product


def index(request):
    products = Product.objects.all()
    active_products = Product.objects.filter(status = "active")
    inactive_products = Product.objects.filter(status = "inactive")

    context = {
        'products':products,
        'active_products': active_products,
        'inactive_products':inactive_products
    }

    return render(request, 'home.html', context)


def my_products(request):
    my_products = Product.objects.filter(user=request.user)

    context = {
        'my_products': my_products
    }

    return render(request, 'my_products.html', context)

@login_required(login_url='login')
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
    else:
        form = ProductForm()

    return render(request, 'new_product.html', {'form': form})

def product_view(request, id):
    product = get_object_or_404(Product, id=id)


    context = {
        'product': product

    }
    return render(request, 'product.html', context)

@login_required(login_url='login')
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST' and product.user == request.user:
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product', id=id)
    else:
        form = ProductForm(instance=product)

    return render(request, 'edit_product.html', {'form': form, 'product': product})

@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, id=id, user=request.user)
    product.delete()
    return redirect('home')