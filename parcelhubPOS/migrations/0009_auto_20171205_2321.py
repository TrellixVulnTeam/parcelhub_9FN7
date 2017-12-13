# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-05 15:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('parcelhubPOS', '0008_auto_20171205_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceitem',
            name='zone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Zone'),
        ),
        migrations.AlterField(
            model_name='statementofaccount',
            name='createtimestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 5, 15, 21, 40, 256229, tzinfo=utc), verbose_name='create timestamp'),
        ),
    ]