from django.shortcuts import render

# Главная галерея/категории товаров
def catalog(request):
    return render(request, 'goods/catalog.html')

def product(reqeuest):
    ()

def girls(request):
    return render(request, 'goods/girls.html')

def boys(request):
    return render(request, 'goods/boys.html')

def adults(request):
    return render(request, 'goods/adults.html')

def extract(request):
    return render(request, 'goods/extract.html')

def balloons(request):
    return render(request, 'goods/balloons.html')

def photobooth(request):
    return render(request, 'goods/photobooth.html')

def other(request):
    return render(request, 'goods/other.html')
