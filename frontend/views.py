from django.shortcuts import render
from .models import *

def Products(request):
    products = Product.objetcs.all()
    return render(request, 'products.html', {'products':products})