# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-05 15:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('parcelhubPOS', '0009_auto_20171205_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statementofaccount',
            name='createtimestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 5, 15, 57, 49, 784319, tzinfo=utc), verbose_name='create timestamp'),
        ),
    ]