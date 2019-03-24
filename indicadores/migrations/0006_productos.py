# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-03-15 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0005_auto_20190315_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200, null=True)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
    ]