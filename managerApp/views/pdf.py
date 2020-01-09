from django.views.generic import View
from django.utils import timezone
from . import *
from managerApp.render import Render
import statistics


class ActPorTerm(View):

    def get(self, request):
        query = self.request.GET.get('terminologia')
        today = timezone.now()
        params = {
            'today': today,
            'term': Term.objects.get(id=query),
            'propuestas': Proposal.objects.filter(term=query),
            'tesis': Thesis.objects.filter(term=query),
            'defensas': Defense.objects.filter(thesis__term=query),
            'request': request
        }
        return Render.render('managerApp/pdf_export/actporterminologia/pdf_lista.html', params) 

class ActPorTermDet(View):

    def get(self, request):
        query = self.request.GET.get('terminologia')
        today = timezone.now()
        params = {
            'today': today,
            'term': Term.objects.get(id=query),
            'propuestas': Proposal.objects.filter(term=query),
            'tesis': Thesis.objects.filter(term=query),
            'defensas': Defense.objects.filter(thesis__term=query),
            'request': request
        }
        return Render.render('managerApp/pdf_export/actporterminologia/pdf_detalle.html', params) 

class StatsNotas(View):

    def get(self, request):
        query = self.request.GET.get('l_terms', '').split(",")
        if(query[0] != ''):
            terms = Term.objects.filter(id__in=query)
        else:
            terms = Term.objects.all()
        data = {
            "terms":[],
            }
        for t in terms:
            data["terms"].append({"name":t.description})
            data["terms"][-1]["notas"] = []
            defensas = Defense.objects.filter(thesis__term=t)
            for d in defensas:
                 data["terms"][-1]["notas"].append(d.grade)
        today = timezone.now()
        params = {
            'today': today,
            'terms': data["terms"],
            'request': request
        }
        return Render.render('managerApp/pdf_export/stats/pdf_notas.html', params) 


class TareasProfesor(View):

    def get(self, request):
        query = self.request.GET.get('profesor')
        today = timezone.now()
        params = {
            'today': today,
            'profesor': Person.objects.get(id=query),
            'propuestas': Proposal.objects.filter(academic_tutor=query),
            'tesis': Thesis.objects.filter(proposal__academic_tutor=query),
            'defensas': Defense.objects.filter(
                 Q(jury_1=query) | Q(jury_2=query) | Q(jury_suplente=query) | Q(thesis__proposal__academic_tutor=query)
            ),
            'request': request
        }
        return Render.render('managerApp/pdf_export/asignadoaprofesor/pdf_lista.html', params) 

class TareasProfesorDetalle(View):

    def get(self, request):
        query = self.request.GET.get('profesor')
        today = timezone.now()
        params = {
            'today': today,
            'profesor': Person.objects.get(id=query),
            'propuestas': Proposal.objects.filter(academic_tutor=query),
            'tesis': Thesis.objects.filter(proposal__academic_tutor=query),
            'defensas': Defense.objects.filter(
                 Q(jury_1=query) | Q(jury_2=query) | Q(jury_suplente=query) | Q(thesis__proposal__academic_tutor=query)
            ),
            'request': request
        }
        return Render.render('managerApp/pdf_export/asignadoaprofesor/pdf_detalle.html', params) 


class DefensasPendientes(View):

    def get(self, request):
        today = timezone.now()
        params = {
            'today': today,
            'defensas': Defense.objects.all().order_by('thesis__proposal__student_1__document_id'),
            'request': request
        }
        return Render.render('managerApp/pdf_export/defensapendiente/pdf_lista.html', params) 

class DefensasPendientesDetalle(View):

    def get(self, request):
        today = timezone.now()
        params = {
            'today': today,
            'defensas': Defense.objects.all().order_by('thesis__proposal__student_1__document_id'),
            'request': request
        }
        return Render.render('managerApp/pdf_export/defensapendiente/pdf_detalle.html', params) 


class TgEjecucion(View):

    def get(self, request):
        today = timezone.now()
        aprobado = ThesisStatus.objects.get(name='Aprobado')
        rechazado = ThesisStatus.objects.get(name='Rechazado')
        params = {
            'today': today,
            'thesis': Thesis.objects.all().exclude(status=aprobado.id).exclude(status=rechazado.id).order_by('proposal__student_1__document_id'),
            'request': request
        }
        return Render.render('managerApp/pdf_export/tgenejecucion/pdf_lista.html', params) 


class TgEjecucionDetalle(View):

    def get(self, request):
        today = timezone.now()
        aprobado = ThesisStatus.objects.get(name='Aprobado')
        rechazado = ThesisStatus.objects.get(name='Rechazado')
        params = {
            'today': today,
            'thesis': Thesis.objects.all().exclude(status=aprobado.id).exclude(status=rechazado.id).order_by('proposal__student_1__document_id'),
            'request': request
        }
        return Render.render('managerApp/pdf_export/tgenejecucion/pdf_detalle.html', params) 


class PropuestasSinAprobar(View):

    def get(self, request):
        today = timezone.now()
        aprobado = ProposalStatus.objects.get(name='Aprobada')
        params = {
            'today': today,
            'propuestas': Proposal.objects.all().exclude(status=aprobado.id).order_by('student_1__document_id'),
            'request': request
        }
        return Render.render('managerApp/pdf_export/propsinaprobar/pdf_lista.html', params) 


class PropuestasSinAprobarDetalle(View):

    def get(self, request):
        today = timezone.now()
        aprobado = ProposalStatus.objects.get(name='Aprobada')
        params = {
            'today': today,
            'propuestas': Proposal.objects.all().exclude(status=aprobado.id).order_by('student_1__document_id'),
            'request': request
        }
        return Render.render('managerApp/pdf_export/propsinaprobar/pdf_detalle.html', params) 