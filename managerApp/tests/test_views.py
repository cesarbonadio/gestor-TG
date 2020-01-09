from django.test import TestCase, Client
from django.urls import reverse
from managerApp.models import Defense, Person, PersonType, Proposal, ProposalStatus, Term, Thesis, ThesisStatus, User
from django.utils import timezone


class TestProposalViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user(username='tester',password='123456',is_guest=True)
		self.user_admin = User.objects.create_user(username='manager',password='123456',is_manager=True)
		self.prop_status = ProposalStatus.objects.create(name='Pendiente')
		self.person_type = PersonType.objects.create(name='Estudiante')
		self.term = Term.objects.create(id=2)
		self.person = Person.objects.create(type = self.person_type,document_id=1,first_name_1='test',last_name_1='test',phone_1=132323)
		self.proposal = Proposal.objects.create(delivery_date=timezone.now(),title='tesis 1',student_1=self.person,academic_tutor=self.person,company_tutor=self.person,term = self.term ,status=self.prop_status)

	def test_home(self):
		response = self.client.get(reverse('home'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'managerApp/home.html')

	def test_login(self):
		login = self.client.login(username='tester',password='123456')
		self.assertTrue(login)

	def test_proposal_list_user_logged_in(self):
		login = self.client.login(username='tester',password='123456')
		response = self.client.get(reverse('proposals:proposals_list'))
		self.assertEqual(response.status_code, 200)
		

	def test_proposal_list_user_not_logged_in(self):
		response = self.client.get(reverse('proposals:proposals_list'))
		self.assertEquals(response.status_code, 302)


	def test_proposal_details_user_logged_in(self):
		login = self.client.login(username='manager',password='123456')
		response = self.client.get(reverse('proposals:proposals_details',args=[1]))
		self.assertEqual(response.status_code, 200)

		

	def test_proposal_details_user_not_logged_in(self):
		response = self.client.get(reverse('proposals:proposals_details', args=[1]))
		self.assertEquals(response.status_code, 302)

	def test_proposal_create_user_logged_in(self):
		login = self.client.login(username='manager',password='123456')
		response = self.client.get(reverse('proposals:proposals_create'))
		self.assertEqual(response.status_code, 200)
		

	def test_proposal_create_user_not_logged_in(self):
		response = self.client.get(reverse('proposals:proposals_create'))
		self.assertEquals(response.status_code, 302)

	def test_proposal_update_user_logged_in(self):
		login = self.client.login(username='manager',password='123456')
		response = self.client.get(reverse('proposals:proposals_update', args=[1]))
		self.assertEqual(response.status_code, 200)

		
	def test_proposal_update_user_not_logged_in(self):
		response = self.client.get(reverse('proposals:proposals_update',args=[1]))
		self.assertEquals(response.status_code, 302)

	def test_proposal_delete_user_logged_in(self):
		login = self.client.login(username='manager',password='123456')
		response = self.client.get(reverse('proposals:proposals_delete',args=[1]))
		self.assertEqual(response.status_code, 200)

	def test_proposal_delete_user_not_logged_in(self):
		response = self.client.get(reverse('proposals:proposals_delete',args=[1]))
		self.assertEquals(response.status_code, 302)

class TestPersonViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user(username='tester2',password='123456',is_guest=True)
		self.user_admin = User.objects.create_user(username='manager2',password='123456',is_manager=True)
		self.person_type = PersonType.objects.create(name='Estudiante')
		self.person = Person.objects.create(type = self.person_type,document_id=1,first_name_1='test',last_name_1='test',phone_1=132323)

	def test_person_list_user_logged_in(self):
		login = self.client.login(username='tester2',password='123456')
		response = self.client.get(reverse('persons:persons_list'))
		self.assertEqual(response.status_code, 200)
		

	def test_person_list_user_not_logged_in(self):
		response = self.client.get(reverse('persons:persons_list'))
		self.assertEquals(response.status_code, 302)
		
	def test_person_details_user_logged_in(self):
		login = self.client.login(username='manager2',password='123456')
		response = self.client.get(reverse('persons:persons_details',args=[1]))
		self.assertEqual(response.status_code, 200)

	def test_person_details_user_not_logged_in(self):
		response = self.client.get(reverse('persons:persons_details', args=[1]))
		self.assertEquals(response.status_code, 302)

	def test_person_create_user_logged_in(self):
		login = self.client.login(username='manager2',password='123456')
		response = self.client.get(reverse('persons:persons_create'))
		self.assertEqual(response.status_code, 200)
		

	def test_person_create_user_not_logged_in(self):
		response = self.client.get(reverse('persons:persons_create'))
		self.assertEquals(response.status_code, 302)

	def test_person_update_user_logged_in(self):
		login = self.client.login(username='manager2',password='123456')
		response = self.client.get(reverse('persons:persons_update', args=[1]))
		self.assertEqual(response.status_code, 200)
		
	def test_person_update_user_not_logged_in(self):
		response = self.client.get(reverse('persons:persons_update',args=[1]))
		self.assertEquals(response.status_code, 302)

	def test_person_delete_user_logged_in(self):
		login = self.client.login(username='manager2',password='123456')
		response = self.client.get(reverse('persons:persons_delete',args=[1]))
		self.assertEqual(response.status_code, 200)

	def test_person_delete_user_not_logged_in(self):
		response = self.client.get(reverse('persons:persons_delete',args=[1]))
		self.assertEquals(response.status_code, 302)

class TestTermViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.user_admin = User.objects.create_user(username='admin2',password='123456',is_admin=True)
		self.person_type = PersonType.objects.create(name='Estudiante')
		self.person = Person.objects.create(type = self.person_type,document_id=1,first_name_1='test',last_name_1='test',phone_1=132323)
		self.term = Term.objects.create(id=3)


	def test_term_list_user_logged_in(self):
		login = self.client.login(username='admin2',password='123456')
		response = self.client.get(reverse('terms:terms_list'))
		self.assertEqual(response.status_code, 200)
		

	def test_term_list_user_not_logged_in(self):
		response = self.client.get(reverse('terms:terms_list'))
		self.assertEquals(response.status_code, 302)
		

	def test_term_create_user_logged_in(self):
		login = self.client.login(username='admin2',password='123456')
		response = self.client.get(reverse('terms:terms_create'))
		self.assertEqual(response.status_code, 200)
		

	def test_term_create_user_not_logged_in(self):
		response = self.client.get(reverse('terms:terms_create'))
		self.assertEquals(response.status_code, 302)

	def test_term_update_user_logged_in(self):
		login = self.client.login(username='admin2',password='123456')
		response = self.client.get(reverse('terms:terms_update',args=[3]))
		self.assertEquals(response.status_code, 200)
		
	def test_term_update_user_not_logged_in(self):
		response = self.client.get(reverse('terms:terms_update',args=[1]))
		self.assertEquals(response.status_code, 302)

	def test_term_delete_user_logged_in(self):
		login = self.client.login(username='admin2',password='123456')
		response = self.client.get(reverse('terms:terms_delete',args=[3]))
		self.assertEqual(response.status_code, 200)

	def test_term_delete_user_not_logged_in(self):
		response = self.client.get(reverse('terms:terms_delete',args=[1]))
		self.assertEquals(response.status_code, 302)

class TestProposalStatusViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.user_admin = User.objects.create_user(username='admin3',password='123456',is_admin=True)
		self.prop_status = ProposalStatus.objects.create(name='En Revision')


	def test_proposal_status_list_user_logged_in(self):
		login = self.client.login(username='admin3',password='123456')
		response = self.client.get(reverse('proposal_status:proposal_status_list'))
		self.assertEqual(response.status_code, 200)
		

	def test_proposal_status_list_user_not_logged_in(self):
		response = self.client.get(reverse('proposal_status:proposal_status_list'))
		self.assertEquals(response.status_code, 302)
		

	def test_proposal_status_create_user_logged_in(self):
		login = self.client.login(username='admin3',password='123456')
		response = self.client.get(reverse('proposal_status:proposal_status_create'))
		self.assertEqual(response.status_code, 200)
		

	def test_proposal_status_create_user_not_logged_in(self):
		response = self.client.get(reverse('proposal_status:proposal_status_create'))
		self.assertEquals(response.status_code, 302)

	def test_proposal_status_update_user_logged_in(self):
		login = self.client.login(username='admin3',password='123456')
		response = self.client.get(reverse('proposal_status:proposal_status_update',args=[3]))
		self.assertEquals(response.status_code, 200)
		
	def test_proposal_status_update_user_not_logged_in(self):
		response = self.client.get(reverse('proposal_status:proposal_status_update',args=[1]))
		self.assertEquals(response.status_code, 302)

	def test_proposal_status_delete_user_logged_in(self):
		login = self.client.login(username='admin3',password='123456')
		response = self.client.get(reverse('proposal_status:proposal_status_delete',args=[3]))
		self.assertEqual(response.status_code, 200)

	def test_proposal_status_delete_user_not_logged_in(self):
		response = self.client.get(reverse('proposal_status:proposal_status_delete',args=[1]))
		self.assertEquals(response.status_code, 302)

class TestThesisStatusViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.user_admin = User.objects.create_user(username='admin4',password='123456',is_admin=True)
		self.thesis_status = ThesisStatus.objects.create(name='En Revision')


	def test_thesis_status_list_user_logged_in(self):
		login = self.client.login(username='admin4',password='123456')
		response = self.client.get(reverse('thesis_status:thesis_status_list'))
		self.assertEqual(response.status_code, 200)
		

	def test_thesis_status_list_user_not_logged_in(self):
		response = self.client.get(reverse('thesis_status:thesis_status_list'))
		self.assertEquals(response.status_code, 302)
		

	def test_thesis_status_create_user_logged_in(self):
		login = self.client.login(username='admin4',password='123456')
		response = self.client.get(reverse('thesis_status:thesis_status_create'))
		self.assertEqual(response.status_code, 200)
		

	def test_thesis_status_create_user_not_logged_in(self):
		response = self.client.get(reverse('thesis_status:thesis_status_create'))
		self.assertEquals(response.status_code, 302)

	def test_thesis_status_update_user_logged_in(self):
		login = self.client.login(username='admin4',password='123456')
		response = self.client.get(reverse('thesis_status:thesis_status_update',args=[3]))
		self.assertEquals(response.status_code, 200)
		
	def test_thesis_status_update_user_not_logged_in(self):
		response = self.client.get(reverse('thesis_status:thesis_status_update',args=[1]))
		self.assertEquals(response.status_code, 302)

	def test_thesis_status_delete_user_logged_in(self):
		login = self.client.login(username='admin4',password='123456')
		response = self.client.get(reverse('thesis_status:thesis_status_delete',args=[3]))
		self.assertEqual(response.status_code, 200)

	def test_thesis_status_delete_user_not_logged_in(self):
		response = self.client.get(reverse('thesis_status:thesis_status_delete',args=[1]))
		self.assertEquals(response.status_code, 302)

class TestThesisViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.thesis_status = ThesisStatus.objects.create(name='pendiente')
		self.user = User.objects.create_user(username='tester3',password='123456',is_guest=True)
		self.user_gestor = User.objects.create_user(username='manager3',password='123456',is_manager=True)

	def test_thesis_list_user_logged_in(self):
		login = self.client.login(username='tester3',password='123456')
		response = self.client.get(reverse('thesis:thesis_list'))
		self.assertEqual(response.status_code, 200)
		

	def test_thesis_list_user_not_logged_in(self):
		response = self.client.get(reverse('thesis:thesis_list'))
		self.assertEquals(response.status_code, 302)
		
	def test_thesis_details_user_logged_in(self):
		login = self.client.login(username='manager3',password='123456')
		response = self.client.get(reverse('thesis:thesis_details',args=[1]))
		self.assertEqual(response.status_code, 404)

	def test_thesis_details_user_not_logged_in(self):
		response = self.client.get(reverse('thesis:thesis_details', args=[1]))
		self.assertEquals(response.status_code, 302)

	def test_thesis_create_user_logged_in(self):
		login = self.client.login(username='manager3',password='123456')
		response = self.client.get(reverse('thesis:thesis_create'))
		self.assertEqual(response.status_code, 200)
		

	def test_thesis_create_user_not_logged_in(self):
		response = self.client.get(reverse('thesis:thesis_create'))
		self.assertEquals(response.status_code, 302)

	def test_thesis_update_user_logged_in(self):
		login = self.client.login(username='manager3',password='123456')
		response = self.client.get(reverse('thesis:thesis_update', args=[1]))
		self.assertEqual(response.status_code,404)
		
	def test_thesis_update_user_not_logged_in(self):
		response = self.client.get(reverse('thesis:thesis_update',args=[1]))
		self.assertEquals(response.status_code, 302)

	def test_thesis_delete_user_logged_in(self):
		login = self.client.login(username='manager3',password='123456')
		response = self.client.get(reverse('thesis:thesis_delete',args=[1]))
		self.assertEqual(response.status_code, 404)

	def test_thesis_delete_user_not_logged_in(self):
		response = self.client.get(reverse('thesis:thesis_delete',args=[1]))
		self.assertEquals(response.status_code, 302)

class TestDefensesViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user(username='tester4',password='123456',is_guest=True)
		self.user_gestor = User.objects.create_user(username='manager4',password='123456',is_manager=True)

	def test_defense_list_user_logged_in(self):
		login = self.client.login(username='tester4',password='123456')
		response = self.client.get(reverse('defense:defense_list'))
		self.assertEqual(response.status_code, 200)
		

	def test_defense_list_user_not_logged_in(self):
		response = self.client.get(reverse('defense:defense_list'))
		self.assertEquals(response.status_code, 302)
		
	def test_defense_details_user_logged_in(self):
		login = self.client.login(username='manager4',password='123456')
		response = self.client.get(reverse('defense:defense_details',args=[1]))
		self.assertEqual(response.status_code, 404)

	def test_defense_details_user_not_logged_in(self):
		response = self.client.get(reverse('defense:defense_details', args=[1]))
		self.assertEquals(response.status_code, 302)

	def test_defense_create_user_logged_in(self):
		login = self.client.login(username='manager4',password='123456')
		response = self.client.get(reverse('defense:defense_create'))
		self.assertEqual(response.status_code, 200)
		

	def test_defense_create_user_not_logged_in(self):
		response = self.client.get(reverse('defense:defense_create'))
		self.assertEquals(response.status_code, 302)

	def test_defense_update_user_logged_in(self):
		login = self.client.login(username='manager4',password='123456')
		response = self.client.get(reverse('defense:defense_update', args=[1]))
		self.assertEqual(response.status_code,404)
		
	def test_defense_update_user_not_logged_in(self):
		response = self.client.get(reverse('defense:defense_update',args=[1]))
		self.assertEquals(response.status_code, 302)

	def test_defense_delete_user_logged_in(self):
		login = self.client.login(username='manager4',password='123456')
		response = self.client.get(reverse('defense:defense_delete',args=[1]))
		self.assertEqual(response.status_code, 404)

	def test_defense_delete_user_not_logged_in(self):
		response = self.client.get(reverse('defense:defense_delete',args=[1]))
		self.assertEquals(response.status_code, 302)

class TestPersonTypeViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.person_type = PersonType.objects.create(name='Profesor')
		self.user_admin = User.objects.create_user(username='admin5',password='123456',is_admin=True)


	def test_person_type_list_user_logged_in(self):
		login = self.client.login(username='admin5',password='123456')
		response = self.client.get(reverse('person_type:person_type_list'))
		self.assertEqual(response.status_code, 200)
		

	def test_person_type_list_user_not_logged_in(self):
		response = self.client.get(reverse('person_type:person_type_list'))
		self.assertEquals(response.status_code, 302)
		

	def test_person_type_create_user_logged_in(self):
		login = self.client.login(username='admin5',password='123456')
		response = self.client.get(reverse('person_type:person_type_create'))
		self.assertEqual(response.status_code, 200)
		

	def test_person_type_create_user_not_logged_in(self):
		response = self.client.get(reverse('person_type:person_type_create'))
		self.assertEquals(response.status_code, 302)

	def test_person_type_update_user_logged_in(self):
		login = self.client.login(username='admin5',password='123456')
		response = self.client.get(reverse('person_type:person_type_update',args=[3]))
		self.assertEquals(response.status_code, 200)
		
	def test_person_type_update_user_not_logged_in(self):
		response = self.client.get(reverse('person_type:person_type_update',args=[1]))
		self.assertEquals(response.status_code, 302)

	def test_person_type_delete_user_logged_in(self):
		login = self.client.login(username='admin5',password='123456')
		response = self.client.get(reverse('person_type:person_type_delete',args=[3]))
		self.assertEqual(response.status_code, 200)

	def test_person_type_delete_user_not_logged_in(self):
		response = self.client.get(reverse('person_type:person_type_delete',args=[1]))
		self.assertEquals(response.status_code, 302)

class TestUserViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user(username='tester5',password='123456',is_guest=True)
		self.user_gestor = User.objects.create_user(username='admin6',password='123456',is_admin=True)

	def test_user_list_user_logged_in(self):
		login = self.client.login(username='admin6',password='123456')
		response = self.client.get(reverse('user:user_list'))
		self.assertEqual(response.status_code, 200)
		

	def test_user_list_user_not_logged_in(self):
		response = self.client.get(reverse('user:user_list'))
		self.assertEquals(response.status_code, 302)
		
	def test_user_details_user_logged_in(self):
		login = self.client.login(username='admin6',password='123456')
		response = self.client.get(reverse('user:user_details',args=[1]))
		self.assertEqual(response.status_code, 200)

	def test_user_details_user_not_logged_in(self):
		response = self.client.get(reverse('user:user_details', args=[1]))
		self.assertEquals(response.status_code, 302)

	def test_user_create_user_logged_in(self):
		login = self.client.login(username='admin6',password='123456')
		response = self.client.get(reverse('user:user_create'))
		self.assertEqual(response.status_code, 200)
		

	def test_user_create_user_not_logged_in(self):
		response = self.client.get(reverse('user:user_create'))
		self.assertEquals(response.status_code, 302)

	def test_user_update_user_logged_in(self):
		login = self.client.login(username='admin6',password='123456')
		response = self.client.get(reverse('user:user_update', args=[1]))
		self.assertEqual(response.status_code,200)
		
	def test_user_update_user_not_logged_in(self):
		response = self.client.get(reverse('user:user_update',args=[1]))
		self.assertEquals(response.status_code, 302)

	def test_user_delete_user_logged_in(self):
		login = self.client.login(username='admin6',password='123456')
		response = self.client.get(reverse('user:user_delete',args=[1]))
		self.assertEqual(response.status_code, 200)

	def test_user_delete_user_not_logged_in(self):
		response = self.client.get(reverse('user:user_delete',args=[1]))
		self.assertEquals(response.status_code, 302)

class TestReportesViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user(username='tester6',password='123456',is_guest=True)
		self.user_admin = User.objects.create_user(username='admin6',password='123456',is_admin=True)
		self.user_gestor = User.objects.create_user(username='gestor6',password='123456',is_manager=True)

	def test_propuestas_sin_aprobar_reporte_view(self):
		login = self.client.login(username='gestor6',password='123456')
		response = self.client.get(reverse('reporte:propsinaprobar')) 
		self.assertEqual(response.status_code, 200)

	# def test_create_propuestas_sin_aprobar_details_reporte_view(self):
	#  	response = self.client.get(reverse('reporte:propsinaprobar_details', args=[1]))
	# 	self.assertEqual(resolve.status_code, 200)

	def test_create_thesis_ejecucion_reporte_view(self):
		login = self.client.login(username='tester6',password='123456')
		response = self.client.get(reverse('reporte:tgenejecucion'))
		self.assertEqual(response.status_code, 200)

	def test_defensa_pendiente_reporte_view(self):
		login = self.client.login(username='tester6',password='123456')
		response = self.client.get(reverse('reporte:defensapendiente'))
		self.assertEqual(response.status_code, 200)


	def test_asignado_profesor_reporte_view(self):
		login = self.client.login(username='tester6',password='123456')
		response = self.client.get(reverse('reporte:asignadoaprofesor'))
		self.assertEqual(response.status_code, 200)

	# def test_tareas_profesor_reporte_view(self):
	# 	response = self.client.get(reverse('reporte:tareasdeprofesor'))
		# self.assertEqual(response.status_code, 200)

	def test_act_terminologia_reporte_view(self):
		login = self.client.login(username='tester6',password='123456')
		response = self.client.get(reverse('reporte:actporterminologia'))
		self.assertEqual(response.status_code, 200)

	# def test_tareas_term_reporte_view(self):
	# 	response = self.client.get(reverse('reporte:tareasporterm'))
		# self.assertEqual(response.status_code, 200)

	def test_estadisticas_reporte_view(self):
		login = self.client.login(username='tester6',password='123456')
		response = self.client.get(reverse('reporte:estadisticas'))
		self.assertEqual(response.status_code, 200)

	# def test_detail_esadisticas_data_reporte_view(self):
	# 	response = self.client.get(reverse('reporte:data_estadisticas'))
		# self.assertEqual(response.status_code, 200)