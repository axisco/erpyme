from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

def index(request):
    params = {}
    params["titulo"] = "Proveedores"
    params["nombre"] = "DJANGO"
    return render (request, 'dashboard/index.html', params)