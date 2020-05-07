from . import *


@method_decorator([login_required, guest_permissions], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'managerApp/proposal/index.html'
    context_object_name = 'latest_propuestas'
    
    def get_queryset(self):
        return Proposal.objects.order_by('-delivery_date')


@method_decorator([login_required, guest_permissions], name='dispatch')
class DetailView(generic.DetailView):
    model = Proposal
    template_name = 'managerApp/proposal/detail.html'


@method_decorator([login_required, manager_permissions], name='dispatch')
class CreateProposalView(generic.CreateView):
    model = Proposal
    fields = "__all__"
    template_name = 'managerApp/proposal/create.html'

    def get_form(self):
        form = super().get_form()
        form.fields['delivery_date'].widget = DateTimePickerInput(
            options = {
                "format": "DD/MM/YYYY hh:mm:ss",
                "locale": "es"
            }
        )
        return form

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

    def get_form(self):
        form = super().get_form()
        form.fields['delivery_date'].widget = DateTimePickerInput(
            options = {
                "format": "DD/MM/YYYY hh:mm:ss",
                "locale": "es"
            }
        )
        return form

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

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Propuesta eliminada exitosamente")
        return super().delete(request, *args, **kwargs)

@method_decorator([login_required, manager_permissions], name='dispatch')
class PropuestasSinAprobarView(generic.ListView):
    model = Proposal
    template_name = 'managerApp/reporte/propsinaprobar/index.html'
    context_object_name = 'propuestas_sin_aprobar'
    success_url = reverse_lazy('reporte:propsinaprobar')
    paginate_by = 15
    def get_queryset(self):
        aprobado = ProposalStatus.objects.get(name='Aprobada')
        return Proposal.objects.all().exclude(status=aprobado.id).order_by('student_1__document_id')

@method_decorator([login_required, guest_permissions], name='dispatch')
class PropuestasSinAprobarDetailView(generic.DetailView):
    model = Proposal
    template_name = 'managerApp/reporte/propsinaprobar/detail.html'