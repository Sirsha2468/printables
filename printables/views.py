from category.models import *
from django.shortcuts import render
from django.http import HttpResponseRedirect

def products(request):
    return render(request, 'products.html')

def home(request):
    return render(request, 'home.html')

def product(request):
    products = Product.objects.all()
    context = {"products" : products}
    return render(request, 'products.html', context)

def product_details(request, pk):
    product = Product.objects.get(pk=pk)    
    context = {"product" : product}
    return render(request, 'product-detail.html', context)
