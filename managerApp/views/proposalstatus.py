from . import *


@method_decorator([login_required, admin_permissions], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'managerApp/proposalstatus/index.html'
    context_object_name = 'proposalstatus_list'
    
    def get_queryset(self):
        return ProposalStatus.objects.order_by('id')


@method_decorator([login_required, admin_permissions], name='dispatch')
class CreateProposalStatusView(generic.CreateView):
    model = ProposalStatus
    fields = "__all__"
    template_name = 'managerApp/proposalstatus/create.html'

    def form_valid(self, form):
        proposalstatus = form.save(commit=False)
        proposalstatus.save()
        messages.success(self.request, 'Fue creao un nuevo tipo de estatus de propuesta')
        return redirect('proposal_status:proposal_status_list')


@method_decorator([login_required, admin_permissions], name='dispatch')
class UpdateProposalStatusView(generic.UpdateView):
    model = ProposalStatus
    fields = "__all__"
    template_name = 'managerApp/proposalstatus/update.html'

    def form_valid(self, form):
        proposalstatus = form.save(commit=False)
        proposalstatus.save()
        messages.success(self.request, 'Fue modificado un tipo de estatus de propuesta')
        return redirect('proposal_status:proposal_status_list')


@method_decorator([login_required, admin_permissions], name='dispatch')
class DeleteProposalStatusView(generic.DeleteView):
    model = ProposalStatus
    template_name = 'managerApp/proposalstatus/delete.html'
    success_url = reverse_lazy('proposal_status:proposal_status_list')
