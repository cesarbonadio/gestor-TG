# Generated by Django 2.2.7 on 2020-01-10 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managerApp', '0006_historicalpersontype_historicalproposalstatus_historicalterm_historicalthesisstatus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AlterField(
            model_name='defense',
            name='grade',
            field=models.IntegerField(blank=True, null=True, verbose_name='calificación'),
        ),
        migrations.AlterField(
            model_name='defense',
            name='jury_suplente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jury_suplente_defense', to='managerApp.Person', verbose_name='jurado suplente'),
        ),
        migrations.AlterField(
            model_name='historicaldefense',
            name='grade',
            field=models.IntegerField(blank=True, null=True, verbose_name='calificación'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Es administrador'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_guest',
            field=models.BooleanField(default=False, verbose_name='Es invitado'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(default=False, verbose_name='Es gestor'),
        ),
    ]