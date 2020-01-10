from django.views.generic import View
from django.utils import timezone
from . import *
from managerApp.render import Render
import statistics
import itertools
       


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
            defensas = Defense.objects.filter(thesis__term=t).filter(grade__isnull=False)
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
            'defensas': Defense.objects.filter(grade__isnull=True).order_by('thesis__proposal__student_1__document_id'),
            'request': request
        }
        return Render.render('managerApp/pdf_export/defensapendiente/pdf_lista.html', params) 

class DefensasPendientesDetalle(View):

    def get(self, request):
        today = timezone.now()
        params = {
            'today': today,
            'defensas': Defense.objects.filter(grade__isnull=True).order_by('thesis__proposal__student_1__document_id'),
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

class ActPorStatus(View):

    def get(self, request):
        status = self.request.GET.get('estatus')
        tipo = self.request.GET.get('tipo')
        term = self.request.GET.get('term')

        today = timezone.now()
        aprobado = ProposalStatus.objects.get(name='Aprobada')
        params = {
            'today': today,
            'terminologia': term,
            'tipo': tipo,
            'status':status,
            'request': request
        }

        if(tipo == '1'):
            params['propuestas'] = Proposal.objects.all().filter(status=status).filter(term=term)
        elif(tipo == '2'):
            params['tesis'] = Thesis.objects.all().filter(status=status).filter(term=term)
        elif(tipo == '3'):
            if(status == 1):
                params['defensas'] = Defense.objects.all().filter(grade__isnull=True).filter(term=term)
            else:
                params['defensas'] = Defense.objects.all().filter(grade__isnull=False).filter(term=term)
        return Render.render('managerApp/pdf_export/actporstatus/pdf_lista.html', params) 

class ActPorStatusDetalle(View):

    def get(self, request):
        status = self.request.GET.get('estatus')
        tipo = self.request.GET.get('tipo')
        term = self.request.GET.get('term')

        today = timezone.now()
        aprobado = ProposalStatus.objects.get(name='Aprobada')
        params = {
            'today': today,
            'terminologia': term,
            'tipo': tipo,
            'status':status,
            'request': request
        }

        if(tipo == '1'):
            params['propuestas'] = Proposal.objects.all().filter(status=status).filter(term=term)
        elif(tipo == '2'):
            params['tesis'] = Thesis.objects.all().filter(status=status).filter(term=term)
        elif(tipo == '3'):
            if(status == 1):
                params['defensas'] = Defense.objects.all().filter(grade__isnull=True).filter(term=term)
            else:
                params['defensas'] = Defense.objects.all().filter(grade__isnull=False).filter(term=term)
        return Render.render('managerApp/pdf_export/actporstatus/pdf_detalle.html', params) 


class LogsTransacciones(View):

    def get(self, request):
       
        actions_executed_persons = Person.history.all()
        actions_executed_defense = Defense.history.all()
        actions_executed_persontype = PersonType.history.all()
        actions_executed_proposals = Proposal.history.all()
        actions_executed_proposalsstatus = ProposalStatus.history.all()
        actions_executed_term = Term.history.all()
        actions_executed_thesisstatus = ThesisStatus.history.all()
        actions_executed_thesis = Thesis.history.all()

        actions_executed = list(itertools.chain(
            actions_executed_persons, 
            actions_executed_defense, 
            actions_executed_persontype,
            actions_executed_proposals,
            actions_executed_proposalsstatus,
            actions_executed_term,
            actions_executed_thesisstatus,
            actions_executed_thesis
        ))

        today = timezone.now()
        params = {
            'today': today,
            'actions_executed': actions_executed,
            'request': request
        }

        return Render.render('managerApp/pdf_export/logporusuario/pdf_lista.html', params) 

# ---------------------------------------
#   Pdf de consultas
# ---------------------------------------
class ProposalIndex(View):
    
    def get(self, request):
        today = timezone.now()
        params = {
            'today': today,
            'propuestas': Proposal.objects.order_by('-delivery_date'),
            'request': request
        }
        return Render.render('managerApp/pdf_export/proposal/pdf_lista.html', params) 

class PersonIndex(View):
    
    def get(self, request):
        query = self.request.GET.get('id')
        if(query):
            personas = Person.objects.filter(id=query).order_by('first_name_1')
        else:
            personas = Person.objects.order_by('first_name_1')
        today = timezone.now()
        params = {
            'today': today,
            'personas': personas,
            'request': request
        }
        return Render.render('managerApp/pdf_export/person/pdf_lista.html', params) 


class TermIndex(View):
    
    def get(self, request):
        today = timezone.now()
        params = {
            'today': today,
            'terms': Term.objects.order_by('-id'),
            'request': request
        }
        return Render.render('managerApp/pdf_export/term/pdf_lista.html', params) 


class ThesisIndex(View):
    
    def get(self, request):
        today = timezone.now()
        params = {
            'today': today,
            'thesis': Thesis.objects.order_by('id'),
            'request': request
        }
        return Render.render('managerApp/pdf_export/thesis/pdf_lista.html', params) 


class DefenseIndex(View):
    
    def get(self, request):
        today = timezone.now()
        params = {
            'today': today,
            'defense': Defense.objects.order_by('thesis'),
            'request': request
        }
        return Render.render('managerApp/pdf_export/defense/pdf_lista.html', params) 


