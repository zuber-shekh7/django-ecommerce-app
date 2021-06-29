from django.shortcuts import render

from slider.models import Slider
from products.models import Product

def index(request):
    sliders = Slider.objects.filter(is_active=True)
    products = Product.objects.filter(is_available=True)[:6]
    context = {
        'sliders': sliders,
        'products':  products,
    }
    return render(request, 'core/index.html', context)


def about(request):
    return render(request, 'core/about.html')