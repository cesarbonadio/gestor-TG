# Generated by Django 2.2.7 on 2019-12-28 07:40

#esta migracion es de datos para cargar los datos iniciales necesarios
from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_proposal_status(apps, schema_editor):
    ProposalStatus = apps.get_model('managerApp', 'ProposalStatus')
    ProposalStatus.objects.create(name='Por evaluar')
    ProposalStatus.objects.create(name='Diferida')
    ProposalStatus.objects.create(name='Aprobada')
    ProposalStatus.objects.create(name='Rechazada')


def create_thesis_status(apps, schema_editor):
    ThesisStatus = apps.get_model('managerApp', 'ThesisStatus')
    ThesisStatus.objects.create(name='Por entregar')
    ThesisStatus.objects.create(name='Entregado y pendiente por defender')
    ThesisStatus.objects.create(name='Diferido')
    ThesisStatus.objects.create(name='Aprobado')
    ThesisStatus.objects.create(name='Aprobado con solicitud de correcciones')
    ThesisStatus.objects.create(name='Rechazado')


def create_terms(apps, schema_editor):
    Term = apps.get_model('managerApp','Term')
    Term.objects.create(id="201915", description='primer semestre del año académico 2019')
    Term.objects.create(id="201925", description='segundo semestre del año académico 2019')


def create_example_users(apps, schema_editor):
    User = apps.get_model('managerApp','User')
    User.objects.create(
        password=make_password("contrasenaAdmin"),
        is_superuser=False,
        username="admin",
        is_admin=True
    )
    User.objects.create(
        password=make_password("contrasenaGestor"),
        is_superuser=False,
        username="gestor",
        is_manager=True
    )
    User.objects.create(
        password=make_password("contrasenainvitado"),
        is_superuser=False,
        username="invitado",
        is_guest=True
    )
    


class Migration(migrations.Migration):

    dependencies = [
        ('managerApp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_proposal_status),
        migrations.RunPython(create_thesis_status),
        migrations.RunPython(create_terms),
        migrations.RunPython(create_example_users)
    ]