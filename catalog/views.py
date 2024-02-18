from django.shortcuts import render


def contacts(request):
    return render(request, 'catalog/contacts.html')


def index(request):
    return render(request, 'catalog/index.html')
