from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.contrib import messages

#importando vistas genéricas
#las vistas genéricas ayudan a ahorrar código
#en caso de que no existan se utilizan funciones
from django.views import generic
from django.urls import reverse, reverse_lazy

from ..models import Proposal
from ..forms import proposalForms




class IndexView(generic.ListView):
    template_name = 'managerApp/proposal/index.html'
    context_object_name = 'latest_propuestas'
    
    def get_queryset(self):
        return Proposal.objects.order_by('-delivery_date')[:5]


class DetailView(generic.DetailView):
    model = Proposal
    template_name = 'managerApp/proposal/detail.html'


class CreateProposalView(generic.CreateView):
    model = Proposal
    fields = "__all__"
    template_name = 'managerApp/proposal/create.html'

    def form_valid(self, form):
        proposal = form.save(commit=False)
        proposal.save()
        messages.success(self.request, 'La propuesta fue creada satisfactoriamente')
        return redirect('proposals:proposals_list')

