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

from ..models import ProposalStatus


class IndexView(generic.ListView):
    template_name = 'managerApp/proposalstatus/index.html'
    context_object_name = 'proposalstatus_list'
    
    def get_queryset(self):
        return ProposalStatus.objects.order_by('id')[:10]


class CreateProposalStatusView(generic.CreateView):
    model = ProposalStatus
    fields = "__all__"
    template_name = 'managerApp/proposalstatus/create.html'

    def form_valid(self, form):
        proposal = form.save(commit=False)
        proposal.save()
        messages.success(self.request, 'Fue creao un nuevo tipo de estatus de propuesta')
        return redirect('proposal_status:proposal_status_list')


class UpdateProposalStatusView(generic.UpdateView):
    model = ProposalStatus
    fields = "__all__"
    template_name = 'managerApp/proposalstatus/update.html'

    def form_valid(self, form):
        proposal = form.save(commit=False)
        proposal.save()
        messages.success(self.request, 'Fue modificado un tipo de estatus de propuesta')
        return redirect('proposal_status:proposal_status_list')


class DeleteProposalStatusView(generic.DeleteView):
    model = ProposalStatus
    template_name = 'managerApp/proposalstatus/delete.html'
    success_url = reverse_lazy('proposal_status:proposal_status_list')
