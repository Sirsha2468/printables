from django.shortcuts import render

def home(request):
    context={}
    return render(request, "store/home.html", context)

def products(request):
    context = {}
    return render(request, "store/products.html", context)

def cart(request):
    context = {}
    return render(request, "store/cart.html", context)

def checkout(request):
    context={}
    return render(request, "store/checkout.html")

def customize(request):
    customize = {}
    return render(request, "store/customize.html")

def contacts(request):
    context={}
    return render(request, "store/contact.html")
