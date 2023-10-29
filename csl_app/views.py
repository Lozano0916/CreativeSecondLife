from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Inicio(TemplateView):
    template_name = 'index.html'

class Login(TemplateView):
    template_name = 'login.html'

class Product(TemplateView):
    template_name = 'product.html'