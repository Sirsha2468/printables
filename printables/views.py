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

def stickers(request):
    category = Category.objects.get(name="Stickers")
    product = Product.objects.filter(category=category)
    return render(request, 'products.html', {
        "products" : product
    })

def posters(request):
    category = Category.objects.get(name="Posters")
    product = Product.objects.filter(category=category)
    return render(request, 'products.html', {
        "products" : product
    })

def t_shirts(request):
    category = Category.objects.get(name="t-shirts")
    product = Product.objects.filter(category=category)
    return render(request, 'products.html', {
        "products" : product
    })

def customise(request):
    # category = Category.objects.get(name="customise")
    # product = Product.objects.filter(category=category)
    return render(request, 'customise.html', {
        "products" : product
    })