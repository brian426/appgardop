# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20160714_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=255, verbose_name='Cargo'),
        ),
    ]
