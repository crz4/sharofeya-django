from django.shortcuts import render

# Главная галерея/категории товаров
def catalog(request):
    return render(request, 'goods/catalog.html')

def product(request):
    return render(request, 'goods/product.html')
