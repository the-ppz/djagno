from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from django.views.generic import TemplateView

# Create your views here.
class Inicio(TemplateView):
    template_name = 'crud/home.html' 
    
class Compras(TemplateView):
    template_name = 'crud/compras.html' 