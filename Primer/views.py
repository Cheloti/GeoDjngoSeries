from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from io import open
from Primer.models import DelitosMuni, Prueba
from . import models
import csv
from geopy import Nominatim
from datetime import date
from django.contrib.gis.geos import GEOSGeometry
import os
from django.conf import settings

path = os.path.join(settings.BASE_DIR, 'Primer/incidentes _modificado.csv')


class index(TemplateView):
    template_name = 'Primer/index.html'


def sectores(request):
    obj = serialize('geojson', models.Incidences.object.all())
    return HttpResponse(obj, content_type='json')


def mencionar(request):
    try:
        url = path
        with open(url) as csvarchivo:
            entrada = csv.reader(csvarchivo)
            # DELITO, DIRECCION, CANTIDAD, ZONA, SUB_ZONA, SUB_ZONA_1, SUB_ZONA_2, MES, SUBURB = next(entrada)
            next(entrada)
            actual = date.today()
            geolocator = Nominatim()
            for i in entrada:
                idfalso, DELITO, DIRECCION, CANTIDAD, ZONA, SUB_ZONA, SUB_ZONA_1, SUB_ZONA_2, MES, SUBURB = i
                location = False
                try:
                    location = geolocator.geocode(str(DIRECCION + " , San Juan Bautista "), timeout=10)
                except Exception:
                    print('error en el location')

                # location = geolocator.geocode(str(DIRECCION + " , San Juan Bautista "), timeout=10)
                for j in range(0, int(CANTIDAD)):
                    delitomuni = DelitosMuni(
                        idfalso=int(idfalso),
                        delito=str(DELITO),
                        direccion=str(DIRECCION),
                        cantidad=int(CANTIDAD),
                        zona=str(ZONA),
                        subzona=str(SUB_ZONA),
                        subzona1=str(SUB_ZONA_1),
                        subzona2=str(SUB_ZONA_2),
                        mes=date(year=2017, month=int(MES), day=2))

                    if location:
                        delitomuni.lat = float(location.latitude)
                        delitomuni.lng = float(location.longitude)
                        delitomuni.punto = GEOSGeometry(
                            'POINT(%s %s), 4326' % (
                                float(location.longitude), float(location.latitude)))
                        delitomuni.nuevadireccion = str(location.address)
                        delitomuni.referenciado = True
                    else:
                        delitomuni.referenciado = False

                    delitomuni.save()
    except Exception:
        print('algo salio mal')

    return render(request, 'Primer/resultado.html', {'muni': 'helow'})


def prueba(request):
    for i in range(0, 9):
        p = Prueba(mensaje="hola carajo 3")
        p.save()
    return render(request, 'Primer/resultado.html', {'muni': 'helow'})
