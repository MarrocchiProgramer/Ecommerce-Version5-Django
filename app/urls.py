from django.urls import path
from django.contrib import admin
from .views import home, carrito, contacto


urlpatterns = [
    path('', home, name="home"),
    path('carrito/', carrito, name="carrito"),
    path('contacto/', contacto, name="contacto")
]




