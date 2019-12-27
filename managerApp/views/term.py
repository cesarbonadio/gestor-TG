from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.contrib import messages
from django.urls import reverse_lazy

from django.views import generic
from django.urls import reverse, reverse_lazy

from ..models import Term


class IndexView(generic.ListView):
    template_name = 'managerApp/term/index.html'
    context_object_name = 'term_list'
    
    def get_queryset(self):
        return Term.objects.order_by('-id')[:5]