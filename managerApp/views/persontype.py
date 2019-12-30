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
from django.utils.decorators import method_decorator
from ..decorators import admin_permissions
from django.contrib.auth.decorators import login_required

from ..models import PersonType


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
