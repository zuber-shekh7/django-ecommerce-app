from django.shortcuts import render

from .models import Product

def list_products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/list.html', context)
