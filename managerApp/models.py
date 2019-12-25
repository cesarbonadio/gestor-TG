from django.db import models
#getText lazy es para enumerar las opciones de ciertos atributos
from django.utils.translation import gettext_lazy as _


'''TODO->VER LO DEL ATRIBUTOS UNIQUE'''
'''TODO->VER LO DEL verbose_name '''
'''TODO->VER SI TODOS LOS ATRIBUTOS FORANEOS LLEVAN ON_DELETE=MODELS.CASCADE'''


#Modelo para las personas
class Person(models.Model):

    PROFESSOR = 'PRO'
    STUDENT = 'EST'
    EXTERNAL = 'EXT'

    TYPE_CHOICES = [
        (PROFESSOR, 'Profesor'),
        (STUDENT, 'Estudiante'),
        (EXTERNAL, 'Externo')
    ]

    type = models.CharField(max_length=20,choices=TYPE_CHOICES)
    document_id = models.IntegerField(unique=True) #cedula
    first_name_1 = models.CharField(max_length=100)
    first_name_2 = models.CharField(max_length=100, null=True)
    last_name_1 = models.CharField(max_length=100)
    last_name_2 = models.CharField(max_length=100, null=True)
    ucab_mail = models.CharField(max_length=100)
    personal_mail = models.CharField(max_length=100)
    phone_1 = models.CharField(max_length=15)
    phone_2 = models.CharField(max_length=15)
    observations = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name_1 + " " + self.last_name_1



#Modelo para la terminología del período
class Term(models.Model):
    
    id = models.CharField(primary_key=True,max_length=6)
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.id + " (" + self.description + ")"



#Modelo para los estados de las propuestas
class ProposalStatus(models.Model):
    
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



#Modelo para los estados de las Tesis
class ThesisStatus(models.Model):
    
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



#Modelo para las propuestas
class Proposal(models.Model):

    delivery_date = models.DateTimeField('fecha de entrega') #fecha de entrega
    title = models.CharField(max_length=200)
    status = models.ForeignKey(ProposalStatus, on_delete=models.CASCADE, related_name="status_proposal")
    student_1 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="student_1_proposal")
    student_2 = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name="student_2_proposal")
    academic_tutor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="academic_tutor_proposal")
    company_tutor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="company_tutor_proposal")
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name="term_proposal")

    def __str__(self):
        return self.title



#Modelo para el trabajo de grado (TG)
class Thesis(models.Model):

    title = models.CharField(max_length=200, null=True)
    status = models.ForeignKey(ThesisStatus, on_delete=models.CASCADE, related_name="status_thesis")
    nrc = models.IntegerField()
    descriptors = models.CharField(max_length=50)
    thematic_category = models.CharField(max_length=50)
    top_date = models.DateTimeField('fecha tope')
    company_name = models.CharField(max_length=100)
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name="term_thesis")
    thesis = models.ForeignKey(Proposal, on_delete=models.CASCADE, related_name="thesis_proposal")


    def __str__(self):
        return self.title



#Modelo para la defensa del trabajo de grado (TG)
class Defense(models.Model):   

    defense_date = models.DateTimeField('fecha de la defensa')
    jury_1_assistance_confirmation = models.BooleanField(default=False)
    jury_2_assistance_confirmation = models.BooleanField(default=False)
    jury_3_assistance_confirmation = models.BooleanField(default=False)
    grade = models.IntegerField() #AGregar validacion de la calificacion
    publication_mention = models.BooleanField(default=False)
    honorific_mention = models.BooleanField(default=False)
    corrections_delivered = models.BooleanField(default=False)
    top_date_corrections = models.DateTimeField('fecha tope de correcciones')
    grade_uploaded = models.BooleanField(default=False)
    observations = models.CharField(max_length=500)
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE, related_name="thesis_defense")

    def __str__(self):
        return self.defense_date

