from django.shortcuts import render
from django.http  import HttpResponse
from django.views.generic import *
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Inicio(LoginRequiredMixin, TemplateView):
    template_name = 'crud/home.html' 
    login_url = 'clientes_app:login'
    
class Compras(LoginRequiredMixin, TemplateView):
    template_name = 'crud/compras.html' 
    login_url = 'clientes_app:login'
