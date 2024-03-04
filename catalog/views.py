from django.shortcuts import render

from catalog.models import Product


def contacts(request):
    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')


def base_product(request):
    return render(request, 'catalog/base_product.html')


def product_pk(request, pk):
    context = {
        'object_list': Product.objects.get(pk=pk),
    }
    return render(request, 'catalog/product_pk.html', context)


def product_list(request):
    context = {
        'object_list': Product.objects.all(),
    }
    return render(request, 'catalog/product_list.html', context)
