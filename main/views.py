from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from goods.models import Product, Category
import requests

# Главная страница
def index(request):
    categories = Category.objects.all()
    return render(request, 'main/index.html', {'categories': categories})

# Каталог товаров
def catalog(request):
    category_slug = request.GET.get('category')
    products = Product.objects.filter(is_active=True)
    category_obj = None

    if category_slug:
        try:
            category_obj = Category.objects.get(slug=category_slug)
            products = products.filter(category=category_obj)
        except Category.DoesNotExist:
            products = Product.objects.none()

    categories = Category.objects.all()
    return render(request, 'main/catalog.html', {
        'categories': categories,
        'products': products,
        'category': category_obj
    })

# Карточка товара
def product(request):
    slug = request.GET.get('slug')
    product_item = get_object_or_404(Product, slug=slug)
    return render(request, 'goods/product.html', {'product': product_item})

# Контакты
def contacts(request):
    return render(request, 'main/contacts.html')

# Отзывы
def reviews(request):
    return render(request, 'main/reviews.html')

# Добавление товара в корзину (AJAX)
def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        if not product_id:
            return JsonResponse({'success': False})

        cart = request.session.get('cart', {})
        if product_id in cart:
            cart[product_id] += 1
        else:
            cart[product_id] = 1

        request.session['cart'] = cart
        request.session.modified = True
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

# Корзина
def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    # Формируем список товаров для отображения
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    if request.method == 'POST' and cart_items:
        # Создаем текст для отправки в Telegram
        message = "📦 Новый заказ:\n"
        for item in cart_items:
            message += f"{item['product'].title} — {item['quantity']} шт — {item['subtotal']} ₽\n"
        message += f"\n💰 Итого: {total} ₽"

        # --- Отправка в Telegram ---
        TOKEN = "твой_telegram_bot_token"      # токен бота
        CHAT_ID = "id_заказчицы"               # id заказчицы
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.get(url, params={"chat_id": CHAT_ID, "text": message})

        request.session['cart'] = {}  # Очистка корзины после отправки
        return redirect('main:index')

    return render(request, 'main/cart.html', {
        'cart_items': cart_items,
        'total': total
    })
