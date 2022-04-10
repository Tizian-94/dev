from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
   # path('', views.home, name="home"),
   # path('products/', views.products, name='products'),

    path('create_order', views.createOrder, name="create_order")
]