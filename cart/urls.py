"""admin1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [


    path('Cart_addproduct', views.user_cart_addproduct, name='user_cart_addproduct'),
    path('Cart', views.user_cart, name='user_cart'),
     path('Checkout', views.checkout, name='checkout'),

    path('Wishlist_addproduct<bookid>', views.user_wishlist_addproduct, name='user_cart_addproduct'),
    path('Wishlist', views.user_wishlist, name='user_wishlist'),
   
]