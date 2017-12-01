from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from . import models


class index(TemplateView):
    template_name = 'Primer/index.html'


def sectores(request):
    obj = serialize('geojson', models.Incidences.object.all())
    return HttpResponse(obj, content_type='json')


def mencionar():
    print('bainga')
    return 'hiohohoho'
