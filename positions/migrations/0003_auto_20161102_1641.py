# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0002_auto_20161102_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contracts.Contract', verbose_name='Contrato'),
        ),
    ]
