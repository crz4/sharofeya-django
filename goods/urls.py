from django.urls import path
from . import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='catalog'),  # Главная страница каталога
    path('product/', views.product, name='product'),
    path('girls/', views.girls, name='girls'),
    path('boys/', views.boys, name='boys'),
    path('adults/', views.adults, name='adults'),
    path('extract/', views.extract, name='extract'),
    path('balloons/', views.balloons, name='balloons'),
    path('photobooth/', views.photobooth, name='photobooth'),
    path('other/', views.other, name='other'),
]
