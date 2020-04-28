from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.db.models import Q, Count
from simple_history.models import HistoricalRecords



'''TODO->VER LO DEL ATRIBUTOS UNIQUE'''

# Para la autenticacion y autorización
# Extender de AbstractUser
class User(AbstractUser):
    is_admin = models.BooleanField(default=False, verbose_name="Es administrador")
    is_manager = models.BooleanField(default=False, verbose_name="Es gestor")
    is_guest = models.BooleanField(default=False, verbose_name="Es invitado")
    history = HistoricalRecords()

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.username

    def save_hashing(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)
    
    def save_without_hashing(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"



#Modelo para el tipo de persona
class PersonType(models.Model):

    name = models.CharField(max_length=50, verbose_name="nombre")
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tipo de persona"
        verbose_name_plural = "Tipos de persona"




#Modelo para las personas
class Person(models.Model):

    type = models.ForeignKey(PersonType, on_delete=models.CASCADE, related_name="type_person",verbose_name="tipo de persona")
    document_id = models.IntegerField(unique=True, verbose_name="cédula")
    first_name_1 = models.CharField(max_length=100, verbose_name="primer nombre")
    first_name_2 = models.CharField(max_length=100, null=True, blank=True, verbose_name="segundo nombre")
    last_name_1 = models.CharField(max_length=100, verbose_name="primer apellido")
    last_name_2 = models.CharField(max_length=100, null=True, blank=True, verbose_name="segundo apellido")
    ucab_mail = models.CharField(max_length=100,verbose_name="correo ucab", null=True, blank=True)
    personal_mail = models.CharField(max_length=100, verbose_name="correo personal")
    phone_1 = models.CharField(max_length=15, verbose_name="teléfono 1")
    phone_2 = models.CharField(max_length=15, verbose_name="teléfono 2", null=True, blank=True)
    observations = models.CharField(max_length=500, verbose_name="observaciones", null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.first_name_1 + " " + self.last_name_1

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"




#Modelo para la terminología del período
class Term(models.Model):
    
    id = models.IntegerField(primary_key=True, verbose_name="código terminología (Ej:201915)")
    description = models.CharField(max_length=50, verbose_name="descripción")
    history = HistoricalRecords()

    def __str__(self):
        return str(self.id) + " (" + self.description + ")"

    class Meta:
        verbose_name = "Terminología"
        verbose_name_plural = "Terminologías"



#Modelo para los estados de las propuestas
class ProposalStatus(models.Model):
    
    name = models.CharField(max_length=20, verbose_name="nombre")
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Estado de propuesta"
        verbose_name_plural = "Estados de propuestas"



#Modelo para los estados de las Tesis
class ThesisStatus(models.Model):
    
    name = models.CharField(max_length=20, verbose_name="nombre")
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Estado de tesis"
        verbose_name_plural = "Estados de tesis"



#Modelo para las propuestas
class Proposal(models.Model):

    delivery_date = models.DateTimeField(verbose_name='fecha de entrega') #fecha de entrega
    title = models.CharField(max_length=200,verbose_name="título")
    status = models.ForeignKey(ProposalStatus, on_delete=models.CASCADE, related_name="status_proposal",verbose_name="estatus de la propuesta")
    student_1 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="student_1_proposal", verbose_name="estudiante 1")
    student_2 = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True, related_name="student_2_proposal", verbose_name="estudiante 2")
    academic_tutor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="academic_tutor_proposal", verbose_name="tutor académico")
    company_tutor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="company_tutor_proposal", verbose_name="tutor_empresarial")
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name="term_proposal", verbose_name="terminología en la que fue entregada")
    history = HistoricalRecords()

    def __str__(self):
        return self.title
    
    def get_id(self):
        return self.id

    class Meta:
        verbose_name = "Propuesta"
        verbose_name_plural = "Propuestas"



#Modelo para el trabajo de grado (TG)
class Thesis(models.Model):

    id = models.CharField(max_length=100,primary_key=True)
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name="título")
    status = models.ForeignKey(ThesisStatus, on_delete=models.CASCADE, related_name="status_thesis", verbose_name="estatus")
    nrc = models.IntegerField(verbose_name="código NRC")
    descriptors = models.CharField(max_length=50, verbose_name="descriptores")
    thematic_category = models.CharField(max_length=50, verbose_name="categoría temática")
    top_date = models.DateTimeField(verbose_name="fecha tope de entrega")
    company_name = models.CharField(max_length=100, verbose_name="nombre de la empresa")
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name="term_thesis", verbose_name="terminología")
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE, related_name="proposal_thesis", verbose_name="propuesta asociada")
    history = HistoricalRecords()


    def __str__(self):
        if self.title==None:
            return str(self.proposal) 
        return self.title

    def get_id(self):
        return self.id

    def save(self, *args, **kwargs):
        self.id = "TG-" + str(self.proposal.get_id())
        super(Thesis, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Tesis"
        verbose_name_plural = "Tesis"



#Modelo para la defensa del trabajo de grado (TG)
class Defense(models.Model):   

    id = models.CharField(max_length=100,primary_key=True)
    defense_date = models.DateTimeField(verbose_name="fecha de la defensa")
    jury_1 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="jury_1_defense", verbose_name="jurado 1")
    jury_2 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="jury_2_defense", verbose_name="jurado 2")
    jury_suplente = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="jury_suplente_defense", verbose_name="jurado suplente", null=True, blank=True)
    jury_1_assistance_confirmation = models.BooleanField(default=False,verbose_name="jurado 1 asiste")
    jury_2_assistance_confirmation = models.BooleanField(default=False,verbose_name="jurado 2 asiste")
    jury_suplente_assistance_confirmation = models.BooleanField(default=False,verbose_name="jurado suplente asiste")
    tutor_assistance_confirmation = models.BooleanField(default=False,verbose_name="tutor asiste")
    grade = models.IntegerField(verbose_name="calificación", null=True, blank=True) #AGregar validacion de la calificacion
    publication_mention = models.BooleanField(default=False,verbose_name="mención publicación")
    honorific_mention = models.BooleanField(default=False,verbose_name="mención honorífica")
    corrections_delivered = models.BooleanField(default=False,verbose_name="se entregaron correcciones")
    top_date_corrections = models.DateTimeField(verbose_name="fecha tope de correcciones")
    grade_uploaded = models.BooleanField(default=False,verbose_name="se subió la calificación")
    observations = models.CharField(max_length=500,verbose_name="observaciones", null=True, blank=True)
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE, related_name="thesis_defense",verbose_name="tesis asociada")
    history = HistoricalRecords()

    def __str__(self):
        return str(self.id) + "-" +  str(self.thesis) +  "-" + str(self.grade) 

    def save_creating(self, *args, **kwargs):
        count_defenses_related = len(list(Defense.objects.filter(thesis=self.thesis.get_id())))
        self.id = "D" + str(count_defenses_related+1) + "-" + str(self.thesis.get_id())
        super(Defense, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Defensa"
        verbose_name_plural = "Defensas"

        