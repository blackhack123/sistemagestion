# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-10-01 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('areas', '0001_initial'),
        ('normas', '0001_initial'),
        ('seguridad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auditores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='areas.Areas')),
                ('id_auditor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridad.Usuario')),
                ('id_norma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='normas.Normas')),
                ('id_proceso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='areas.Procesos')),
                ('proceso_clausula', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='normas.ProcesoClausula')),
            ],
        ),
        migrations.CreateModel(
            name='Auditorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_auditoria', models.CharField(blank=True, max_length=50, null=True)),
                ('lugar', models.CharField(max_length=50)),
                ('fec_inicio', models.DateField()),
                ('hora_inicio', models.TimeField(blank=True, null=True)),
                ('fec_fin', models.DateField()),
                ('hora_fin', models.TimeField(blank=True, null=True)),
                ('objetivo', models.CharField(max_length=100)),
                ('id_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areas.Areas')),
                ('id_auditor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auditoria.Auditores')),
                ('id_clausula', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='normas.Clausulas')),
                ('id_norma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='normas.Normas')),
                ('id_proceso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='areas.Procesos')),
            ],
        ),
    ]