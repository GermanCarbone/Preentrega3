from django.shortcuts import render
from django.http import HttpResponse
from .models import Fiscal

# Create your views here.
def index(request):
    return render(request, "aplicacion/index.html")

def fiscales(request):
    return render(request, "aplicacion/fiscales.html")

def establecimientos(request):
    return render(request, "aplicacion/establecimientos.html")

def distritos(request):
    return render(request, "aplicacion/distritos.html")

def fiscalForm(request):
    if request.method== "POST":
        fiscal = Fiscal(nombre=request.POST['nombre'], apellido=request.POST['apellido'], dni=request.POST['dni'], telefono=request.POST['telefono'], distrito=request.POST['telefono'])
        fiscal.save()
        return HttpResponse("Fiscal guardado exitosamente")

    return render(request, "aplicacion/fiscalForm.html")