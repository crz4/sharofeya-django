from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def catalog(request):
    return render(request, 'main/catalog.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def reviews(request):
    return render(request, 'main/reviews.html')

def cart(request):
    return render(request, 'main/cart.html')
