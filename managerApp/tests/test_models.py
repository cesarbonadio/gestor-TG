from django.test import TestCase
from managerApp.models import Defense, Person, PersonType, Proposal, ProposalStatus, Term, Thesis, ThesisStatus, User
from django.utils import timezone


class TestPersonTypeModel(TestCase):
	def test_string_reesentation(self):
		person_type = PersonType.objects.create(name='Estudiante')
		self.assertEqual(str(person_type), person_type.name)

class TestDefenseModel(TestCase):
	def test_string_reesentation(self):
		thesis_status = ThesisStatus.objects.create(name='En Revision')
		person_type = PersonType.objects.create(name='Estudiante')
		prop_status = ProposalStatus.objects.create(name='Pendiente')
		person = Person.objects.create(type = person_type,document_id=1,first_name_1='test',last_name_1='test',phone_1=132323)
		term = Term.objects.create(id=2)
		proposal = Proposal.objects.create(delivery_date=timezone.now(),title='tesis 1',student_1=person,academic_tutor=person,company_tutor=person,term = term ,status=prop_status)
		thesis = Thesis.objects.create(title='Tesis Prueba', status= thesis_status, nrc = 1234, descriptors="TEst",thematic_category="Test 2", top_date= timezone.now(), company_name= "COmpania", term= term,proposal=proposal)

		defense = Defense.objects.create(defense_date=timezone.now() + timezone.timedelta(days=2), jury_1=person,jury_2=person,jury_suplente=person,jury_1_assistance_confirmation=True,jury_2_assistance_confirmation=True,jury_suplente_assistance_confirmation=True,tutor_assistance_confirmation=True,grade=2,thesis=thesis,top_date_corrections=timezone.now() + timezone.timedelta(days=20))
		self.assertEqual(str(defense), str(defense.id) + "-" +  str(defense.thesis) +  "-" + str(defense.grade))

class TestProposalModel(TestCase):
	def test_string_reesentation(self):
		person_type = PersonType.objects.create(name='Estudiante')
		prop_status = ProposalStatus.objects.create(name='Pendiente')
		person = Person.objects.create(type = person_type,document_id=1,first_name_1='test',last_name_1='test',phone_1=132323)
		term = Term.objects.create(id=2)
		proposal = Proposal.objects.create(delivery_date=timezone.now(),title='tesis 1',student_1=person,academic_tutor=person,company_tutor=person,term = term ,status=prop_status)
		self.assertEqual(str(proposal), proposal.title)

class TestProposalStatusModel(TestCase):
	def test_string_reesentation(self):
		prop_status = ProposalStatus.objects.create(name='Pendiente')
		self.assertEqual(str(prop_status), prop_status.name)

class TestTermModel(TestCase):
	def test_string_reesentation(self):
		term = Term.objects.create(id=2)
		self.assertEqual(str(term), str(term.id) + " (" + term.description + ")")

class TestThesisModel(TestCase):
	def test_string_reesentation(self):
		thesis_status = ThesisStatus.objects.create(name='En Revision')
		person_type = PersonType.objects.create(name='Estudiante')
		prop_status = ProposalStatus.objects.create(name='Pendiente')
		person = Person.objects.create(type = person_type,document_id=1,first_name_1='test',last_name_1='test',phone_1=132323)
		term = Term.objects.create(id=2)
		proposal = Proposal.objects.create(delivery_date=timezone.now(),title='tesis 1',student_1=person,academic_tutor=person,company_tutor=person,term = term ,status=prop_status)
		thesis = Thesis.objects.create(title='Tesis Prueba', status= thesis_status, nrc = 1234, descriptors="TEst",thematic_category="Test 2", top_date= timezone.now(), company_name= "COmpania", term= term,proposal=proposal)
		self.assertEqual(str(thesis), thesis.title)

class TestThesisStatusModel(TestCase):
	def test_string_reesentation(self):
		thesis_status = ThesisStatus.objects.create(name='En Revision')
		self.assertEqual(str(thesis_status), thesis_status.name)

class TestUserModel(TestCase):
	def test_string_reesentation(self):
		user = User.objects.create_user(username='tester',password='123456',is_guest=True)
		self.assertEqual(str(user), user.username)

class TestPersonModel(TestCase):
	def test_string_reesentation(self):
		person_type = PersonType.objects.create(name='Estudiante')
		person = Person.objects.create(type = person_type,document_id=1,first_name_1='test',last_name_1='test',phone_1=132323)
		self.assertEqual(str(person), person.first_name_1 + " " + person.last_name_1)


