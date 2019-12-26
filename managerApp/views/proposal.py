from django.shortcuts import render
from django.http import HttpResponse
from ..models import Proposal
from django.template import loader
from django.http import Http404

#importando vistas genéricas
#las vistas genéricas ayudan a ahorrar código
#en caso de que no existan se utilizan funciones
from django.views import generic
from django.urls import reverse, reverse_lazy


class IndexView(generic.ListView):
    template_name = 'managerApp/proposal/index.html'
    context_object_name = 'latest_propuestas'
    
    def get_queryset(self):
        return Proposal.objects.order_by('-delivery_date')[:5]


class DetailView(generic.DetailView):
    model = Proposal
    template_name = 'managerApp/proposal/detail.html'
    


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


