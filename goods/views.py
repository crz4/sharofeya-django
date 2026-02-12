from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def catalog(request):
    category_slug = request.GET.get('category')  # получаем параметр из URL
    products = Product.objects.filter(is_active=True)  # все активные по умолчанию

    category_obj = None
    if category_slug:
        try:
            category_obj = Category.objects.get(slug=category_slug)
            products = products.filter(category=category_obj)
        except Category.DoesNotExist:
            products = Product.objects.none()  # если категория не найдена

    context = {
        'products': products,
        'category': category_obj,
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    slug = request.GET.get('slug')  # получаем slug товара из URL
    product_item = get_object_or_404(Product, slug=slug)  # если не найден, 404
    context = {
        'product': product_item,
    }
    return render(request, 'goods/product.html', context)
