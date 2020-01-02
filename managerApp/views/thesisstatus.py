from . import *

@method_decorator([login_required, admin_permissions], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'managerApp/thesisstatus/index.html'
    context_object_name = 'thesisstatus_list'
    
    def get_queryset(self):
        return ThesisStatus.objects.order_by('id')


@method_decorator([login_required, admin_permissions], name='dispatch')
class CreateThesisStatusView(generic.CreateView):
    model = ThesisStatus
    fields = "__all__"
    template_name = 'managerApp/thesisstatus/create.html'

    def form_valid(self, form):
        thesisstatus = form.save(commit=False)
        thesisstatus.save()
        messages.success(self.request, 'Fue creao un nuevo tipo de estatus de tesis')
        return redirect('thesis_status:thesis_status_list')


@method_decorator([login_required, admin_permissions], name='dispatch')
class UpdateThesisStatusView(generic.UpdateView):
    model = ThesisStatus
    fields = "__all__"
    template_name = 'managerApp/thesisstatus/update.html'

    def form_valid(self, form):
        thesisstatus = form.save(commit=False)
        thesisstatus.save()
        messages.success(self.request, 'Fue modificado un tipo de estatus de tesis')
        return redirect('thesis_status:thesis_status_list')


@method_decorator([login_required, admin_permissions], name='dispatch')
class DeleteThesisStatusView(generic.DeleteView):
    model = ThesisStatus
    template_name = 'managerApp/thesisstatus/delete.html'
    success_url = reverse_lazy('thesis_status:thesis_status_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Estatus de tesis eliminado exitosamente")
        return super().delete(request, *args, **kwargs)
