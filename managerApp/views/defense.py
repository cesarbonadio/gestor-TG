from . import *


# para no repetir
DEFENSE_CRUD_FIELDS = (
    "defense_date",
    "jury_1_assistance_confirmation",
    "jury_2_assistance_confirmation",
    "jury_3_assistance_confirmation",
    "grade",
    "publication_mention",
    "honorific_mention",
    "corrections_delivered",
    "top_date_corrections",
    "grade_uploaded",
    "observations",
    "thesis"
)


@method_decorator([login_required, guest_permissions], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'managerApp/defense/index.html'
    context_object_name = 'defense_list'
    
    def get_queryset(self):
        return Defense.objects.order_by('thesis')


@method_decorator([login_required, guest_permissions], name='dispatch')
class DetailView(generic.DetailView):
    model = Defense
    template_name = 'managerApp/defense/detail.html'


@method_decorator([login_required, manager_permissions], name='dispatch')
class CreateDefenseView(generic.CreateView):
    model = Defense
    fields = DEFENSE_CRUD_FIELDS
    template_name = 'managerApp/defense/create.html'

    def form_valid(self, form):
        defense = form.save(commit=False)
        defense.save_creating()
        messages.success(self.request, 'La defensa fue creada satisfactoriamente')
        return redirect('defense:defense_list')


@method_decorator([login_required, manager_permissions], name='dispatch')
class UpdateDefenseView(generic.UpdateView):
    model = Defense
    fields = DEFENSE_CRUD_FIELDS
    template_name = 'managerApp/defense/update.html'

    def form_valid(self, form):
        defense = form.save(commit=False)
        defense.save()
        messages.success(self.request, 'La defensa fue actualizada satisfactoriamente')
        return redirect('defense:defense_list')


@method_decorator([login_required, manager_permissions], name='dispatch')
class DeleteDefenseView(generic.DeleteView):
    model = Defense
    template_name = 'managerApp/defense/delete.html'
    success_url = reverse_lazy('defense:defense_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "La defensa fue eliminada exitosamente")
        return super().delete(request, *args, **kwargs)