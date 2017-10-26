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
