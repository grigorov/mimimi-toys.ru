from django.shortcuts import render
from landing.models import Toys
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.http import Http404

def index(request):
    toys = Toys.objects.all()
    return (render_to_response('index.html',
       {
      'toys': toys,
       },  context_instance=RequestContext(request))
       )
