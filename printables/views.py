from django.http import HttpResponseRedirect
from django.shortcuts import render
from category.models import *

def home(request):
    products = Product.objects.all()
    context = {"products" : products}
    return render(request, 'home.html', context)

def product_details(request, pk):
    product = Product.objects.get(pk=pk)    
    context = {"product" : product}
    return render(request, 'product-detail.html', context)
