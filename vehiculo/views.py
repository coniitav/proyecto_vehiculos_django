from django.shortcuts import render, redirect
from .models import Vehiculo
from datetime import date

# Create your views here.
def index(request):
    return render(request, "vehiculo/index.html")

def add(request):    
    if request.method == "POST":
        data = request.POST.copy()

        vehiculo = Vehiculo()
        vehiculo.marca = data["marca"]
        vehiculo.modelo = data["modelo"]
        vehiculo.serial_carroceria = data["serial_carro"]
        vehiculo.serial_motor = data["serial_motor"]
        vehiculo.categoria = data["categoria"]
        vehiculo.precio = data["precio"]
        vehiculo.fecha_creacion = date.today()
        vehiculo.fecha_modificacion = date.today()
        vehiculo.save()

        return redirect("/")

    return render(request, "vehiculo/add.html")