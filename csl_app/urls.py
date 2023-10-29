from django.urls import path
from .views import Inicio, Login, Product

urlpatterns=[
    path('inicio', Inicio.as_view(), name='inicio'),
    path('login', Login.as_view(), name='login'),
    path('product', Product.as_view(), name='product'),
]