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
from ..models import *