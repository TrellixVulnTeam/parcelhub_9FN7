# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-10 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcelhubPOS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='identificationno',
            field=models.CharField(max_length=50, unique=True, verbose_name='*Registration/IC No'),
        ),
    ]