from django.test import SimpleTestCase
from django.urls import reverse, resolve
from managerApp.views.proposal import CreateProposalView, IndexView as IndexProposalView, UpdateProposalView, DetailView as DetailProposalView, DeleteProposalView, PropuestasSinAprobarView, PropuestasSinAprobarDetailView

from managerApp.views.person import CreatePersonView, IndexView as IndexPersonView, UpdatePersonView,DetailView as DetailPersonView, DeletePersonView, SelectorDeReporteView, TareasPorProfesorView

from managerApp.views.term import CreateTermView, IndexView as IndexTermView, UpdateTermView, DeleteTermView, SelectorTermView, TareasPorTermView

from managerApp.views.proposalstatus import CreateProposalStatusView, DeleteProposalStatusView, IndexView as IndexProposalStatusView, UpdateProposalStatusView

from managerApp.views.thesisstatus import CreateThesisStatusView, DeleteThesisStatusView, UpdateThesisStatusView, IndexView as IndexThesisStatusView

from managerApp.views.thesis import CreateThesisView, DeleteThesisView, DetailView as DetailThesisView, IndexView as IndexThesisView, UpdateThesisView, ThesisEnEjecucionView

from managerApp.views.defense import CreateDefenseView, DeleteDefenseView, DetailView as DetailDefenseView, IndexView as IndexDefenseView, UpdateDefenseView, DefensaPendienteView, TermSelectorView

from managerApp.views.persontype import CreatePersonTypeView, DeletePersonTypeView, UpdatePersonTypeView, IndexView as IndexPersonTypeView

from managerApp.views.user import CreateUserView, DeleteUserView, UpdateUserView, DetailView as DetailUserView, IndexView as IndexUserView
from managerApp.views import managerApp

class TestUrls(SimpleTestCase):
	def test_home_url(self):
		url = reverse('home')
		self.assertEqual(resolve(url).func, managerApp.home)

class TestProposalUrls(SimpleTestCase):
	def test_index_proposals_url(self):
		url = reverse('proposals:proposals_list')
		self.assertEqual(resolve(url).func.view_class, IndexProposalView)

	def test_details_proposals_url(self):
		url = reverse('proposals:proposals_details', args=[1])
		self.assertEqual(resolve(url).func.view_class, DetailProposalView)

	def test_create_proposals_url(self):
		url = reverse('proposals:proposals_create')
		self.assertEqual(resolve(url).func.view_class, CreateProposalView)

	def test_update_proposals_url(self):
		url = reverse('proposals:proposals_update',args=[1])
		self.assertEqual(resolve(url).func.view_class,UpdateProposalView)

	def test_delete_proposals_url(self):
		url = reverse('proposals:proposals_delete',args=[1])
		self.assertEqual(resolve(url).func.view_class, DeleteProposalView)

class TestPersonsUrls(SimpleTestCase):
	def test_index_persons_url(self):
		url = reverse('persons:persons_list')
		self.assertEqual(resolve(url).func.view_class, IndexPersonView)

	def test_details_persons_url(self):
		url = reverse('persons:persons_details', args=[1])
		self.assertEqual(resolve(url).func.view_class, DetailPersonView)

	def test_create_persons_url(self):
		url = reverse('persons:persons_create')
		self.assertEqual(resolve(url).func.view_class, CreatePersonView)

	def test_update_persons_url(self):
		url = reverse('persons:persons_update',args=[1])
		self.assertEqual(resolve(url).func.view_class,UpdatePersonView)

	def test_delete_persons_url(self):
		url = reverse('persons:persons_delete',args=[1])
		self.assertEqual(resolve(url).func.view_class, DeletePersonView)

class TestTermsUrls(SimpleTestCase):

	def test_index_terms_url(self):
		url = reverse('terms:terms_list')
		self.assertEqual(resolve(url).func.view_class, IndexTermView)

	def test_create_terms_url(self):
		url = reverse('terms:terms_create')
		self.assertEqual(resolve(url).func.view_class, CreateTermView)

	def test_update_terms_url(self):
		url = reverse('terms:terms_update',args=[1])
		self.assertEqual(resolve(url).func.view_class,UpdateTermView)

	def test_delete_terms_url(self):
		url = reverse('terms:terms_delete',args=[1])
		self.assertEqual(resolve(url).func.view_class, DeleteTermView)

class TestProposalStatusUrls(SimpleTestCase):

	def test_index_proposal_status_url(self):
		url = reverse('proposal_status:proposal_status_list')
		self.assertEqual(resolve(url).func.view_class, IndexProposalStatusView)

	def test_create_proposal_status_url(self):
		url = reverse('proposal_status:proposal_status_create')
		self.assertEqual(resolve(url).func.view_class, CreateProposalStatusView)

	def test_update_proposal_status_url(self):
		url = reverse('proposal_status:proposal_status_update',args=[1])
		self.assertEqual(resolve(url).func.view_class,UpdateProposalStatusView)

	def test_delete_proposal_status_url(self):
		url = reverse('proposal_status:proposal_status_delete',args=[1])
		self.assertEqual(resolve(url).func.view_class, DeleteProposalStatusView)

class TestThesisStatusUrls(SimpleTestCase):

	def test_index_thesis_status_url(self):
		url = reverse('thesis_status:thesis_status_list')
		self.assertEqual(resolve(url).func.view_class, IndexThesisStatusView)

	def test_create_thesis_status_url(self):
		url = reverse('thesis_status:thesis_status_create')
		self.assertEqual(resolve(url).func.view_class, CreateThesisStatusView)

	def test_update_thesis_status_url(self):
		url = reverse('thesis_status:thesis_status_update',args=[1])
		self.assertEqual(resolve(url).func.view_class,UpdateThesisStatusView)

	def test_delete_thesis_status_url(self):
		url = reverse('thesis_status:thesis_status_delete',args=[1])
		self.assertEqual(resolve(url).func.view_class, DeleteThesisStatusView)

class TestThesisUrls(SimpleTestCase):
	def test_index_thesis_url(self):
		url = reverse('thesis:thesis_list')
		self.assertEqual(resolve(url).func.view_class, IndexThesisView)

	def test_details_thesis_url(self):
		url = reverse('thesis:thesis_details', args=[1])
		self.assertEqual(resolve(url).func.view_class, DetailThesisView)

	def test_create_thesis_url(self):
		url = reverse('thesis:thesis_create')
		self.assertEqual(resolve(url).func.view_class, CreateThesisView)

	def test_update_thesis_url(self):
		url = reverse('thesis:thesis_update',args=[1])
		self.assertEqual(resolve(url).func.view_class,UpdateThesisView)

	def test_delete_thesis_url(self):
		url = reverse('thesis:thesis_delete',args=[1])
		self.assertEqual(resolve(url).func.view_class, DeleteThesisView)

class TestDefenseUrls(SimpleTestCase):
	def test_index_defense_url(self):
		url = reverse('defense:defense_list')
		self.assertEqual(resolve(url).func.view_class, IndexDefenseView)

	def test_details_defense_url(self):
		url = reverse('defense:defense_details', args=[1])
		self.assertEqual(resolve(url).func.view_class, DetailDefenseView)

	def test_create_defense_url(self):
		url = reverse('defense:defense_create')
		self.assertEqual(resolve(url).func.view_class, CreateDefenseView)

	def test_update_defense_url(self):
		url = reverse('defense:defense_update',args=[1])
		self.assertEqual(resolve(url).func.view_class,UpdateDefenseView)

	def test_delete_defense_url(self):
		url = reverse('defense:defense_delete',args=[1])
		self.assertEqual(resolve(url).func.view_class, DeleteDefenseView)

class TestPersonTypeUrls(SimpleTestCase):
	def test_index_person_type_url(self):
		url = reverse('person_type:person_type_list')
		self.assertEqual(resolve(url).func.view_class, IndexPersonTypeView)

	def test_create_person_type_url(self):
		url = reverse('person_type:person_type_create')
		self.assertEqual(resolve(url).func.view_class, CreatePersonTypeView)

	def test_update_person_type_url(self):
		url = reverse('person_type:person_type_update',args=[1])
		self.assertEqual(resolve(url).func.view_class,UpdatePersonTypeView)

	def test_delete_person_type_url(self):
		url = reverse('person_type:person_type_delete',args=[1])
		self.assertEqual(resolve(url).func.view_class, DeletePersonTypeView)

class TestUsersUrls(SimpleTestCase):
	def test_index_user_url(self):
		url = reverse('user:user_list')
		self.assertEqual(resolve(url).func.view_class, IndexUserView)

	def test_create_user_url(self):
		url = reverse('user:user_create')
		self.assertEqual(resolve(url).func.view_class, CreateUserView)

	def test_update_user_url(self):
		url = reverse('user:user_update',args=[1])
		self.assertEqual(resolve(url).func.view_class,UpdateUserView)

	def test_delete_user_url(self):
		url = reverse('user:user_delete',args=[1])
		self.assertEqual(resolve(url).func.view_class, DeleteUserView)

	def test_detail_user_url(self):
		url = reverse('user:user_details',args=[1])
		self.assertEqual(resolve(url).func.view_class, DetailUserView)

class TestReportesUrls(SimpleTestCase):
	def test_propuestas_sin_aprobar_reporte_url(self):
		url = reverse('reporte:propsinaprobar')
		self.assertEqual(resolve(url).func.view_class, PropuestasSinAprobarView)

	def test_create_propuestas_sin_aprobar_details_reporte_url(self):
	 	url = reverse('reporte:propsinaprobar_details', args=[1])
	 	self.assertEqual(resolve(url).func.view_class, PropuestasSinAprobarDetailView)

	def test_create_thesis_ejecucion_reporte_url(self):
	 	url = reverse('reporte:tgenejecucion')
	 	self.assertEqual(resolve(url).func.view_class, ThesisEnEjecucionView)

	def test_defensa_pendiente_reporte_url(self):
		url = reverse('reporte:defensapendiente')
		self.assertEqual(resolve(url).func.view_class,DefensaPendienteView)


	def test_asignado_profesor_reporte_url(self):
		url = reverse('reporte:asignadoaprofesor')
		self.assertEqual(resolve(url).func.view_class, SelectorDeReporteView)

	def test_tareas_profesor_reporte_url(self):
		url = reverse('reporte:tareasdeprofesor')
		self.assertEqual(resolve(url).func.view_class, TareasPorProfesorView)

	def test_act_terminologia_reporte_url(self):
		url = reverse('reporte:actporterminologia')
		self.assertEqual(resolve(url).func.view_class, SelectorTermView)

	def test_tareas_term_reporte_url(self):
		url = reverse('reporte:tareasporterm')
		self.assertEqual(resolve(url).func.view_class, TareasPorTermView)

	def test_estadisticas_reporte_url(self):
		url = reverse('reporte:estadisticas')
		self.assertEqual(resolve(url).func.view_class, TermSelectorView)

	def test_detail_esadisticas_data_reporte_url(self):
		url = reverse('reporte:data_estadisticas')
		self.assertEqual(resolve(url).func,TermSelectorView.get_data)