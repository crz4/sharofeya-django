from django.shortcuts import render
from goods.models import Category


def index(request):
    categories = Category.objects.all()
    return render(request, 'main/index.html', {
        'categories': categories
    })


def catalog(request):
    categories = Category.objects.all()
    return render(request, 'main/catalog.html', {
        'categories': categories
    })


def contacts(request):
    return render(request, 'main/contacts.html')


def reviews(request):
    return render(request, 'main/reviews.html')


def cart(request):
    return render(request, 'main/cart.html')
