from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from . import models


class index(TemplateView):
    template_name = 'Primer/index.html'


def sectores(request):
    sector = serialize('geojson', models.Sector.objects.all())
    return HttpResponse(sector, content_type='json')
