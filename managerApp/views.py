from django.shortcuts import render
from django.http import HttpResponse
from .models import Proposal
from django.template import loader
from django.http import Http404

# Create your views here.

def index(request):
    latest_propuestas = Proposal.objects.order_by('-fecha_entrega')[:5]
    template = loader.get_template('propuestas/index.html')
    context = {
        'latest_propuestas': latest_propuestas
    }
    return HttpResponse(template.render(context, request))

def detail(request, propuesta_id):
    try:
        propuesta = Proposal.objects.get(pk=propuesta_id)
    except Propuesta.DoesNotExist:
        raise Http404("La propuesta no existe")
    return render(request, 'propuestas/detail.html', {'propuesta': propuesta})


def results(request, propuesta_id):
    response = "Está buscando los resultados de la propuesta %s."
    return HttpResponse(response % propuesta_id)

def modify(request, propuesta_id):
    return HttpResponse("Está modificando la propuesta %s." % propuesta_id)


