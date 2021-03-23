from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirectHome, name='book-red'),
    path('home/', views.home, name='book-home'),
    path('about/', views.about, name='book-about'),
    path('products/', views.products, name='book-products'),
    path('contact/', views.contact, name='book-contact'),
    path('cart/', views.cart, name='cart'),
    path('update_cart/', views.updateCart, name='updated_item'),
]
