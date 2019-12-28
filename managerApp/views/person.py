from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from ..decorators import *
from django.contrib.auth.decorators import login_required
from ..models import Person


@method_decorator([login_required, guest_permissions], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'managerApp/person/index.html'
    context_object_name = 'list_of_persons'
    
    def get_queryset(self):
        return Person.objects.order_by('first_name_1')[:5]

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
