from django.contrib.gis import admin
from .models import Incidences


class IncidentesAdmin(admin.ModelAdmin): #Para listar de forma ordenada en el admin
    list_display = ['name', 'descripcion']


admin.site.register(Incidences, IncidentesAdmin)
