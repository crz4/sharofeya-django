from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Product, Category


def catalog(request):
    category_slug = request.GET.get('category')
    search_query = request.GET.get('q')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    sort = request.GET.get('sort')

    categories = Category.objects.filter(parent__isnull=True)
    category_obj = None
    products = Product.objects.filter(is_active=True)  # Все активные товары по умолчанию
    subcategories = None

    if category_slug:
        category_obj = get_object_or_404(Category, slug=category_slug)
        subcategories = category_obj.subcategories.all()

        # Берем товары текущей категории + прямые подкатегории
        category_ids = [category_obj.id] + list(subcategories.values_list('id', flat=True))
        products = products.filter(category_id__in=category_ids)

    # Поиск по названию и описанию
    if search_query:
        products = products.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    # Фильтр по цене
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Сортировка
    if sort == "new":
        products = products.order_by('-id')
    elif sort == "price_asc":
        products = products.order_by('price')
    elif sort == "price_desc":
        products = products.order_by('-price')

    context = {
        'categories': categories,
        'category': category_obj,
        'subcategories': subcategories,
        'products': products,
    }

    return render(request, 'goods/catalog.html', context)


def product(request):
    slug = request.GET.get('slug')
    product_item = get_object_or_404(Product, slug=slug)

    context = {
        'product': product_item,
    }

    return render(request, 'goods/product.html', context)


def search_products(request):
    query = request.GET.get('q')
    results = []

    if query:
        products = Product.objects.filter(
            title__icontains=query,
            is_active=True
        )[:5]

        results = [{"title": p.title} for p in products]

    return JsonResponse({"results": results})


@require_POST
def add_to_cart(request):
    product_id = request.POST.get('product_id')

    if not product_id:
        return JsonResponse({'success': False})

    # получаем корзину из сессии
    cart = request.session.get('cart', {})

    # если товар уже есть — увеличиваем количество
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart
    request.session.modified = True

    return JsonResponse({'success': True})
