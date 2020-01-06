from . import *
from django.http import JsonResponse
import statistics

# para no repetir
DEFENSE_CRUD_FIELDS = (
    "defense_date",
    "jury_1",
    "jury_2",
    "jury_suplente",
    "jury_1_assistance_confirmation",
    "jury_2_assistance_confirmation",
    "jury_suplente_assistance_confirmation",
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

@method_decorator([login_required, guest_permissions], name='dispatch')
class DefensaPendienteView(generic.ListView):
    model = Defense
    template_name = 'managerApp/reporte/defensapendiente/index.html'
    context_object_name = 'defense_list'
    success_url = reverse_lazy('reporte:defensapendiente')
    paginate_by = 15
    
    def get_queryset(self):
        return Defense.objects.all().order_by('thesis__proposal__student_1__document_id')

@method_decorator([login_required, guest_permissions], name='dispatch')
class TermSelectorView(generic.ListView):
    model = Term
    template_name = 'managerApp/reporte/stats/index.html'
    context_object_name = 'term_list'
    success_url = reverse_lazy('reporte:estadisticas')
    paginate_by = 15
    
    def get_context_data(self, **kwargs):
        context = super(TermSelectorView, self).get_context_data(**kwargs)
        context.update({
            'terms': Person.objects.all(),
            'defensas': Defense.objects.all(),
        })
        return context

    def get_queryset(self):
        return Term.objects.all()

    def get_data(self, **kwargs):
        query = self.GET.get('l_terms', '').split(",")
        if(query[0] != ''):
            terms = Term.objects.filter(id__in=query)
        else:
            terms = Term.objects.all()
        data = {
            "terms":[],
            "notas":[],
            "media":[],
            "mediana":[],
            "moda":[],
            "desviacion":[]
            }
        for t in terms:
            data["terms"].append(t.description)
            data["notas"].append([])
            defensas = Defense.objects.filter(thesis__term=t)
            for d in defensas:
                data["notas"][-1].append(d.grade)
            data["media"].append(statistics.mean(data["notas"][-1]))
            data["mediana"].append(statistics.median(data["notas"][-1]))
            try:
                data["moda"].append(statistics.mode(data["notas"][-1]))
            except statistics.StatisticsError as e:
                data["moda"].append(sorted(data["notas"][-1])[len(data["notas"][-1])//2 - 1])
            data["desviacion"].append(statistics.stdev(data["notas"][-1]))
        
        return JsonResponse(data)

