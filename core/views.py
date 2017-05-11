from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Category

def index(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'pages/index.html', context)


def contact(request):
    return render(request, 'pages/contact.html')


def product_list(request):
    return render(request, 'pages/product_list.html')


def product(request):
    return render(request, 'pages/product.html')