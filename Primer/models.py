from django.contrib.gis.db import models


# Create your models here.

class Incidences(models.Model):
    name = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=210)
    ubicacion = models.PointField(srid=4326)
    object = models.GeoManager()

    def __str__(self):
        return self.name


class Sector(models.Model):
    nombre = models.CharField(max_length=80)
    ubicacion = models.PolygonField(srid=4326)

    def __str__(self):
        return self.nombre


class Lineas(models.Model):
    nombre = models.CharField(max_length=80)
    ubicacion = models.LineStringField(srid=4326)

    def __str__(self):
        return self.nombre


class Multipunt(models.Model):
    nombre = models.CharField(max_length=80)
    ubicacion = models.MultiPointField(srid=4326)

    def __str__(self):
        return self.nombre


# DELITO,DIRECCION,CANTIDAD,ZONA,SUB ZONA,SUB ZONA 1,SUB ZONA 2,MES,SUBURB
class DelitosMuni(models.Model):
    idfalso = models.IntegerField(blank=True, null=True)
    delito = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    nuevadireccion = models.CharField(max_length=400, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    zona = models.CharField(max_length=5, blank=True, null=True)
    subzona = models.CharField(max_length=5, blank=True, null=True)
    subzona1 = models.CharField(max_length=5, blank=True, null=True)
    subzona2 = models.CharField(max_length=5, blank=True, null=True)
    mes = models.DateField()
    punto = models.PointField(srid=4326, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    referenciado = models.BooleanField(default=False)
    object = models.GeoManager()

    def __str__(self):
        return self.direccion + " " + self.delito


class Prueba(models.Model):
    mensaje = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return str(self.mensaje)
