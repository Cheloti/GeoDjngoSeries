from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
# from django.contrib.gis.db import OSMGeoAdmin
from .models import *

"""
class IncidentesAdmin(LeafletGeoAdmin):  # Para listar de forma ordenada en el admin
    list_display = ['name', 'descripcion']
"""

admin.site.register(Incidences, LeafletGeoAdmin)
admin.site.register(Sector, LeafletGeoAdmin)
admin.site.register(Lineas, LeafletGeoAdmin)
admin.site.register(Multipunt, LeafletGeoAdmin)
