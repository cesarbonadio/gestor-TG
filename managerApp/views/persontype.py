from . import *


@method_decorator([login_required, admin_permissions], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'managerApp/persontype/index.html'
    context_object_name = 'person_type_list'
    
    def get_queryset(self):
        return PersonType.objects.order_by('id')[:10]


@method_decorator([login_required, admin_permissions], name='dispatch')
class CreatePersonTypeView(generic.CreateView):
    model = PersonType
    fields = "__all__"
    template_name = 'managerApp/persontype/create.html'

    def form_valid(self, form):
        persontype = form.save(commit=False)
        persontype.save()
        messages.success(self.request, 'Fue creado un nuevo tipo de persona')
        return redirect('person_type:person_type_list')


@method_decorator([login_required, admin_permissions], name='dispatch')
class UpdatePersonTypeView(generic.UpdateView):
    model = PersonType
    fields = "__all__"
    template_name = 'managerApp/persontype/update.html'

    def form_valid(self, form):
        persontype = form.save(commit=False)
        persontype.save()
        messages.success(self.request, 'Fue actualizado un tipo de persona')
        return redirect('person_type:person_type_list')


@method_decorator([login_required, admin_permissions], name='dispatch')
class DeletePersonTypeView(generic.DeleteView):
    model = PersonType
    template_name = 'managerApp/persontype/delete.html'
    success_url = reverse_lazy('person_type:person_type_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "El tipo de persona fue eliminado exitosamente")
        return super().delete(request, *args, **kwargs)
