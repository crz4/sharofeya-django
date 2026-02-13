from django.urls import path
from . import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='catalog'),  
    path('product/', views.product, name='product'), 
    path('search/', views.search_products, name='search_products'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),

]
