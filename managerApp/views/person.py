from . import *


@method_decorator([login_required, guest_permissions], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'managerApp/person/index.html'
    context_object_name = 'list_of_persons'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'filtro_personas': Person.objects.order_by('first_name_1'),
            'id_filtrado': self.request.GET.get('id')
        })
        return context

    def get_queryset(self):
        query = self.request.GET.get('id')
        if(query):
            return Person.objects.filter(id=query).order_by('first_name_1')
        return Person.objects.order_by('first_name_1')

@method_decorator([login_required, guest_permissions], name='dispatch')
class DetailView(generic.DetailView):
    model = Person
    template_name = 'managerApp/person/detail.html'


@method_decorator([login_required, manager_permissions], name='dispatch')
class CreatePersonView(generic.CreateView):
    model = Person
    fields = "__all__"
    template_name = 'managerApp/person/create.html'

    def form_valid(self, form):
        person = form.save(commit=False)
        person.save()
        messages.success(self.request, 'La persona fue creada satisfactoriamente')
        return redirect('persons:persons_list')


@method_decorator([login_required, manager_permissions], name='dispatch')
class UpdatePersonView(generic.UpdateView):
    model = Person
    fields = "__all__"
    template_name = 'managerApp/person/update.html'

    def form_valid(self, form):
        person = form.save(commit=False)
        person.save()
        messages.success(self.request, 'La persona fue actualizada satisfactoriamente')
        return redirect('persons:persons_list')


@method_decorator([login_required, manager_permissions], name='dispatch')
class DeletePersonView(generic.DeleteView):
    model = Person
    template_name = 'managerApp/person/delete.html'
    success_url = reverse_lazy('persons:persons_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "La persona fue eliminada exitosamente")
        return super().delete(request, *args, **kwargs)

@method_decorator([login_required, guest_permissions], name='dispatch')
class SelectorDeReporteView(generic.ListView):
    template_name = 'managerApp/reporte/asignadoaprofesor/index.html'
    context_object_name = 'list_of_persons'
    def get_queryset(self):
        profesor = PersonType.objects.get(name='Profesor')
        return Person.objects.all().filter(type=profesor.id)

@method_decorator([login_required, guest_permissions], name='dispatch')
class TareasPorProfesorView(generic.ListView):
    template_name = 'managerApp/reporte/asignadoaprofesor/index.html'
    context_object_name = 'list_of_persons'
    model = Person

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('profesor')
        context = super(TareasPorProfesorView, self).get_context_data(**kwargs)
        context.update({
            'profesor': Person.objects.get(id=query),
            'propuestas': Proposal.objects.all().filter(academic_tutor=query),
            'tesis': Thesis.objects.all().filter(proposal__academic_tutor=query),
            'defensas': Defense.objects.filter(
                 Q(jury_1=query) | Q(jury_2=query) | Q(jury_suplente=query) | Q(thesis__proposal__academic_tutor=query)
            ),

        })
        return context

    def get_queryset(self):
        profesor = PersonType.objects.get(name='Profesor')
        return Person.objects.all().filter(type=profesor.id)