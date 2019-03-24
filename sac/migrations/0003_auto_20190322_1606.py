# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-03-22 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sac', '0002_sac_sac'),
    ]

    operations = [
        migrations.AddField(
            model_name='planaccion',
            name='detalleRecursoFinanciero',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='planaccion',
            name='detalleRecursoHumano',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='planaccion',
            name='detalleRecursoTecnico',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='planaccion',
            name='recursoFinanciero',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='planaccion',
            name='recursoHumano',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='planaccion',
            name='recursoTecnico',
            field=models.IntegerField(null=True),
        ),
    ]