from django.contrib import admin
from vehiculo.models import Vehiculo

# Register your models here.
@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    pass
