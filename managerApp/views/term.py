from . import *

@method_decorator([login_required, admin_permissions], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'managerApp/term/index.html'
    context_object_name = 'term_list'
    
    def get_queryset(self):
        return Term.objects.order_by('-id')


@method_decorator([login_required, admin_permissions], name='dispatch')
class CreateTermView(generic.CreateView):
    model = Term
    fields = "__all__"
    template_name = 'managerApp/term/create.html'

    def form_valid(self, form):
        term = form.save(commit=False)
        term.save()
        messages.success(self.request, 'La terminología fue creada satisfactoriamente')
        return redirect('terms:terms_list')


@method_decorator([login_required, admin_permissions], name='dispatch')
class UpdateTermView(generic.UpdateView):
    model = Term
    fields = "__all__"
    template_name = 'managerApp/term/update.html'

    def form_valid(self, form):
        term = form.save(commit=False)
        term.save()
        messages.success(self.request, 'La terminología fue actualizada satisfactoriamente')
        return redirect('terms:terms_list')


@method_decorator([login_required, admin_permissions], name='dispatch')
class DeleteTermView(generic.DeleteView):
    model = Term
    template_name = 'managerApp/term/delete.html'
    success_url = reverse_lazy('terms:terms_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Terminología eliminada exitosamente")
        return super().delete(request, *args, **kwargs)

@method_decorator([login_required, guest_permissions], name='dispatch')
class SelectorTermView(generic.ListView):
    template_name = 'managerApp/reporte/actporterminologia/index.html'
    context_object_name = 'list_of_terms'
    def get_queryset(self):
        return Term.objects.all()

@method_decorator([login_required, guest_permissions], name='dispatch')
class TareasPorTermView(generic.ListView):
    template_name = 'managerApp/reporte/actporterminologia/index.html'
    context_object_name = 'list_of_terms'
    model = Term

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('terminologia')
        context = super(TareasPorTermView, self).get_context_data(**kwargs)
        context.update({
            'terminologia': Term.objects.get(id=query),
            'propuestas': Proposal.objects.all().filter(term=query),
            'tesis': Thesis.objects.all().filter(term=query),
            'defensas': Defense.objects.all(),
        })
        return context

    def get_queryset(self):
        return Term.objects.all()