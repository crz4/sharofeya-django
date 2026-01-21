from django.urls import path
from . import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='catalog'),  # Один каталог для всех категорий
    path('product/', views.product, name='product'),  # Если нужна страница отдельного товара
]
