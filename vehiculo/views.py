from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
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

def sign_up(request):
    return render(request, "vehiculo/sign_up.html")

def sign_up_create(request):
    if request.method == "POST":
        data = request.POST.copy()

        nuevo_user = User.objects.filter(username = data["username"]).first()
        if nuevo_user is not None:
            messages.error(request, "Este email ya está registrado")
            return redirect("/sign_up")
        
        nuevo_permiso = Permission.objects.filter(codename = "visualizar_catalogo").first()
        if nuevo_permiso is None:
            content_type = ContentType.objects.get_for_model(Vehiculo)
            nuevo_permiso = Permission()
            nuevo_permiso.codename = "visualizar_catalogo"
            nuevo_permiso.name = "Puede visualizar el catálogo de los vehículos"
            nuevo_permiso.content_type = content_type
            nuevo_permiso.save()
        
        if nuevo_user is None:
            nuevo_user = User()
            nuevo_user.username = data["username"]
            nuevo_user.first_name = data["nombres"]
            nuevo_user.last_name = data["apellidos"]
            nuevo_user.email = data["email"]
            nuevo_user.is_active = True
            nuevo_user.save()

            nuevo_user.set_password(data["password"])
            nuevo_user.user_permissions.add(nuevo_permiso)
            nuevo_user.save()
            messages.success(request, "Usuario creado con éxito")

    return redirect("/sign_in")

def sign_in(request):
    from django.contrib.auth import authenticate, login
    if request.method == "POST":
        data = request.POST.copy()
        username = data["username"]
        password = data["password"]

        usuario_valido = authenticate(request, username = username, password = password)

        if usuario_valido is not None:
            login(request, usuario_valido)
            return redirect("/")
        else:
            messages.error(request, "Usuario o contraseña incorrecto")
            pass

    return render(request, "vehiculo/sign_in.html")

def sign_out(request):
    from django.contrib.auth import logout
    logout(request)
    messages.success(request, "Sesión cerrada")
    return redirect("/")

def listar(request):
    vehiculos = Vehiculo.objects.all()
    context = {
        "vehiculos": vehiculos
    }
    return render(request, "vehiculo/listar.html", context)