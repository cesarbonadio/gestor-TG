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
from ..models import Thesis

# para no repetir
THESIS_CRUD_FIELDS = ("title","status","nrc","descriptors","thematic_category","top_date","company_name","term","proposal")


class IndexView(generic.ListView):
    template_name = 'managerApp/thesis/index.html'
    context_object_name = 'thesis_list'
    
    def get_queryset(self):
        return Thesis.objects.order_by('id')[:10]


class DetailView(generic.DetailView):
    model = Thesis
    template_name = 'managerApp/thesis/detail.html'


class CreateThesisView(generic.CreateView):
    model = Thesis
    fields = THESIS_CRUD_FIELDS
    template_name = 'managerApp/thesis/create.html'

    def form_valid(self, form):
        thesis = form.save(commit=False)
        thesis.save()
        messages.success(self.request, 'La thesis fue creada satisfactoriamente')
        return redirect('thesis:thesis_list')


class UpdateThesisView(generic.UpdateView):
    model = Thesis
    fields = THESIS_CRUD_FIELDS
    template_name = 'managerApp/thesis/update.html'

    def form_valid(self, form):
        proposal = form.save(commit=False)
        proposal.save()
        messages.success(self.request, 'La propuesta fue actualizada satisfactoriamente')
        return redirect('thesis:thesis_list')


class DeleteThesisView(generic.DeleteView):
    model = Thesis
    template_name = 'managerApp/thesis/delete.html'
    success_url = reverse_lazy('thesis:thesis_list')