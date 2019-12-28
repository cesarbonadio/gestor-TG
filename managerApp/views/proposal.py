from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.contrib import messages
from django.urls import reverse_lazy

#importando vistas genéricas
#las vistas genéricas ayudan a ahorrar código
#en caso de que no existan se utilizan funciones
from django.views import generic
from django.urls import reverse, reverse_lazy

from ..models import Proposal
from ..forms import proposalForms

from django.utils.decorators import method_decorator
from ..decorators import *
from django.contrib.auth.decorators import login_required



@method_decorator([login_required, guest_permissions], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'managerApp/proposal/index.html'
    context_object_name = 'latest_propuestas'
    
    def get_queryset(self):
        return Proposal.objects.order_by('-delivery_date')[:5]


@method_decorator([login_required, guest_permissions], name='dispatch')
class DetailView(generic.DetailView):
    model = Proposal
    template_name = 'managerApp/proposal/detail.html'


@method_decorator([login_required, manager_permissions], name='dispatch')
class CreateProposalView(generic.CreateView):
    model = Proposal
    fields = "__all__"
    template_name = 'managerApp/proposal/create.html'

    def form_valid(self, form):
        proposal = form.save(commit=False)
        proposal.save()
        messages.success(self.request, 'La propuesta fue creada satisfactoriamente')
        return redirect('proposals:proposals_list')

@method_decorator([login_required, manager_permissions], name='dispatch')
class UpdateProposalView(generic.UpdateView):
    model = Proposal
    fields = "__all__"
    template_name = 'managerApp/proposal/update.html'

    def form_valid(self, form):
        proposal = form.save(commit=False)
        proposal.save()
        messages.success(self.request, 'La propuesta fue actualizada satisfactoriamente')
        return redirect('proposals:proposals_list')

@method_decorator([login_required, manager_permissions], name='dispatch')
class DeleteProposalView(generic.DeleteView):
    model = Proposal
    template_name = 'managerApp/proposal/delete.html'
    success_url = reverse_lazy('proposals:proposals_list')