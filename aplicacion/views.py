from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "aplicacion/index.html")

def fiscales(request):
    return render(request, "aplicacion/fiscales.html")

def establecimientos(request):
    return render(request, "aplicacion/establecimientos.html")

def distritos(request):
    return render(request, "aplicacion/distritos.html")