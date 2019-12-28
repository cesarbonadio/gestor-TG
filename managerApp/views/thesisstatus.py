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


from ..models import ThesisStatus


@method_decorator([login_required, admin_permissions], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'managerApp/thesisstatus/index.html'
    context_object_name = 'thesisstatus_list'
    
    def get_queryset(self):
        return ThesisStatus.objects.order_by('id')[:10]


@method_decorator([login_required, admin_permissions], name='dispatch')
class CreateThesisStatusView(generic.CreateView):
    model = ThesisStatus
    fields = "__all__"
    template_name = 'managerApp/thesisstatus/create.html'

    def form_valid(self, form):
        proposal = form.save(commit=False)
        proposal.save()
        messages.success(self.request, 'Fue creao un nuevo tipo de estatus de tesis')
        return redirect('thesis_status:thesis_status_list')


@method_decorator([login_required, admin_permissions], name='dispatch')
class UpdateThesisStatusView(generic.UpdateView):
    model = ThesisStatus
    fields = "__all__"
    template_name = 'managerApp/thesisstatus/update.html'

    def form_valid(self, form):
        proposal = form.save(commit=False)
        proposal.save()
        messages.success(self.request, 'Fue modificado un tipo de estatus de tesis')
        return redirect('thesis_status:thesis_status_list')


@method_decorator([login_required, admin_permissions], name='dispatch')
class DeleteThesisStatusView(generic.DeleteView):
    model = ThesisStatus
    template_name = 'managerApp/thesisstatus/delete.html'
    success_url = reverse_lazy('thesis_status:thesis_status_list')
