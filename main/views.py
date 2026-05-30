from django.shortcuts import render

# Create your views here.

from main.models import Product, News


def home(request):
    news = News.objects.order_by('-created_at')
    return render(request, 'home.html', {'news': news})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})